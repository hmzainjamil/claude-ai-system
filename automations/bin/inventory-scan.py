#!/usr/bin/env python3
"""
INVENTORY MESH SCANNER
Discovers all installed tools, models, skills, agents, MCPs, repos
and writes a unified registry that every component can query.
"""

import json
import os
import subprocess
import glob
import sys
from pathlib import Path
from datetime import datetime

REGISTRY = Path.home() / ".claude" / "inventory" / "registry.json"
REGISTRY.parent.mkdir(parents=True, exist_ok=True)

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, text=True).strip()
    except:
        return ""

def scan_skills():
    skills = []
    for p in glob.glob(str(Path.home() / ".claude/skills/*/SKILL.md")):
        name = Path(p).parent.name
        try:
            with open(p) as f:
                lines = f.read().splitlines()
            desc = next((l.lstrip("#").strip() for l in lines if l.strip()), name)
        except:
            desc = name
        skills.append({"name": name, "path": p, "desc": desc[:120]})
    return skills

def scan_ollama_models():
    out = run("ollama list")
    models = []
    for line in out.splitlines()[1:]:
        parts = line.split()
        if parts:
            models.append({"name": parts[0], "size": parts[2] if len(parts) > 2 else "?"})
    return models

def scan_mcp_servers():
    mcp_file = Path.home() / ".mcp.json"
    servers = []
    if mcp_file.exists():
        with open(mcp_file) as f:
            d = json.load(f)
        for k, v in d.get("mcpServers", {}).items():
            servers.append({"name": k, "config": v})
    return servers

def scan_bin_tools():
    tools = []
    bin_dir = Path.home() / ".claude/bin"
    if bin_dir.exists():
        for p in sorted(bin_dir.iterdir()):
            if p.suffix in (".py", ".sh", "") and p.is_file():
                tools.append({"name": p.name, "path": str(p), "type": p.suffix or "bin"})
    return tools

def scan_mae_modules():
    modules = []
    mae_dir = Path.home() / "mae-master-automation-engine"
    if mae_dir.exists():
        for p in sorted(mae_dir.iterdir()):
            if p.is_dir() or p.suffix in (".py", ".sh"):
                modules.append({"name": p.name, "path": str(p)})
    return modules

def scan_tcc_commands():
    cmds = []
    tcc_dir = Path.home() / "tcc-task-command-center"
    if tcc_dir.exists():
        for p in sorted(tcc_dir.iterdir()):
            if p.is_file() and not p.name.startswith("."):
                cmds.append({"name": p.name, "path": str(p)})
    return cmds

def scan_installed_repos():
    repos = []
    for d in glob.glob(str(Path.home() / "installed-repos/*")):
        p = Path(d)
        if p.is_dir():
            readme = p / "README.md"
            desc = ""
            if readme.exists():
                try:
                    with open(readme) as f:
                        desc = f.read(200).splitlines()[0].lstrip("#").strip()
                except:
                    pass
            repos.append({"name": p.name, "path": str(p), "desc": desc[:100]})
    return repos

def scan_python_packages():
    pkgs_raw = run("pip3 list --format=freeze 2>/dev/null | head -80")
    pkgs = []
    KEY = ["anthropic","openai","google-generativeai","groq","ollama","langchain",
           "fastapi","flask","celery","redis","psycopg2","sqlalchemy","reportlab",
           "playwright","selenium","requests","httpx","pydantic","crewai","autogen"]
    installed = {line.split("==")[0].lower() for line in pkgs_raw.splitlines() if "==" in line}
    for k in KEY:
        if k.lower() in installed:
            pkgs.append(k)
    return pkgs

def scan_paperclip():
    try:
        import urllib.request
        urllib.request.urlopen("http://127.0.0.1:3100/health", timeout=2)
        return {"status": "running", "url": "http://127.0.0.1:3100"}
    except:
        return {"status": "offline"}

def scan_llm_routes():
    routes = []
    # Ollama
    if run("curl -s http://localhost:11434/api/tags | python3 -c 'import sys,json; print(\"ok\")' 2>/dev/null"):
        routes.append({"name": "ollama", "endpoint": "http://localhost:11434", "status": "up"})
    else:
        routes.append({"name": "ollama", "status": "down"})
    # Check env keys
    for k, label in [("GROQ_API_KEY","groq"),("GEMINI_API_KEY","gemini"),
                     ("OPENAI_API_KEY","openai"),("DEEPSEEK_API_KEY","deepseek"),
                     ("ANTHROPIC_API_KEY","anthropic")]:
        if os.environ.get(k) or run(f"grep -r '{k}' ~/.zshrc ~/.zprofile 2>/dev/null | head -1"):
            routes.append({"name": label, "status": "configured"})
    return routes

def build_registry():
    print("Scanning inventory...")
    reg = {
        "updated": datetime.now().isoformat(),
        "skills": scan_skills(),
        "ollama_models": scan_ollama_models(),
        "mcp_servers": scan_mcp_servers(),
        "bin_tools": scan_bin_tools(),
        "mae_modules": scan_mae_modules(),
        "tcc_commands": scan_tcc_commands(),
        "installed_repos": scan_installed_repos(),
        "python_packages": scan_python_packages(),
        "paperclip": scan_paperclip(),
        "llm_routes": scan_llm_routes(),
    }
    with open(REGISTRY, "w") as f:
        json.dump(reg, f, indent=2)

    # Summary
    print(f"\n{'='*50}")
    print("INVENTORY MESH — REGISTRY BUILT")
    print(f"{'='*50}")
    print(f"  Skills:          {len(reg['skills'])}")
    print(f"  Ollama models:   {len(reg['ollama_models'])}")
    print(f"  MCP servers:     {len(reg['mcp_servers'])}")
    print(f"  Bin tools:       {len(reg['bin_tools'])}")
    print(f"  MAE modules:     {len(reg['mae_modules'])}")
    print(f"  TCC commands:    {len(reg['tcc_commands'])}")
    print(f"  Repos:           {len(reg['installed_repos'])}")
    print(f"  Python packages: {len(reg['python_packages'])}")
    print(f"  LLM routes:      {len(reg['llm_routes'])}")
    print(f"  Paperclip:       {reg['paperclip']['status']}")
    print(f"\nRegistry: {REGISTRY}")
    return reg

if __name__ == "__main__":
    build_registry()
