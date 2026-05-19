#!/usr/bin/env python3
"""
INVENTORY MESH ROUTER
Any component calls this to: query what's available, find best tool for a task,
get connection instructions, or auto-wire two components together.

Usage:
  inventory-mesh.py query <keyword>         -- find components matching keyword
  inventory-mesh.py best <task>             -- get best tool/model for a task
  inventory-mesh.py wire <comp_a> <comp_b>  -- generate glue code to connect two components
  inventory-mesh.py status                  -- live status of all components
  inventory-mesh.py refresh                 -- rebuild registry
"""

import json
import sys
import os
import subprocess
from pathlib import Path

REGISTRY = Path.home() / ".claude" / "inventory" / "registry.json"

def load():
    if not REGISTRY.exists():
        print("Registry empty — running scan...")
        subprocess.run(["python3", str(Path.home() / ".claude/bin/inventory-scan.py")])
    with open(REGISTRY) as f:
        return json.load(f)

def query(keyword):
    reg = load()
    kw = keyword.lower()
    results = []

    for skill in reg.get("skills", []):
        if kw in skill["name"].lower() or kw in skill.get("desc","").lower():
            results.append(f"[SKILL]  {skill['name']}  —  {skill['desc'][:80]}")

    for m in reg.get("ollama_models", []):
        if kw in m["name"].lower():
            results.append(f"[MODEL]  {m['name']}  ({m['size']})")

    for t in reg.get("bin_tools", []) + reg.get("tools", []):
        if kw in t["name"].lower():
            results.append(f"[TOOL]   {t['name']}  ({t.get('type','registered')})")

    for r in reg.get("installed_repos", []):
        if kw in r["name"].lower() or kw in r.get("desc","").lower():
            results.append(f"[REPO]   {r['name']}  —  {r.get('desc','')[:80]}")

    for m in reg.get("mcp_servers", []):
        if kw in m["name"].lower():
            results.append(f"[MCP]    {m['name']}")

    if results:
        print(f"\nMatches for '{keyword}':")
        for r in results:
            print(f"  {r}")
    else:
        print(f"No matches for '{keyword}'")

def best(task):
    reg = load()
    task_l = task.lower()
    rec = []

    # LLM routing logic
    if any(w in task_l for w in ["fast","quick","simple","classify","json"]):
        models = [m["name"] for m in reg.get("ollama_models", [])]
        if models:
            rec.append(f"LLM: {models[0]} (local/fast)")
        routes = [r for r in reg.get("llm_routes",[]) if r["name"] in ("groq","gemini") and r["status"]=="configured"]
        if routes:
            rec.append(f"LLM: {routes[0]['name']} (cloud/fast)")

    if any(w in task_l for w in ["pdf","report","document"]):
        rec.append("SKILL: reportlab-pdf-master")
        rec.append("TOOL: doc-factory.py")

    if any(w in task_l for w in ["scrape","web","crawl","extract"]):
        rec.append("MCP: Apify")
        rec.append("SKILL: apify-ultimate-scraper")

    if any(w in task_l for w in ["email","outreach","sequence"]):
        rec.append("SKILL: email-sequence")
        rec.append("SKILL: cold-email")

    if any(w in task_l for w in ["agent","automate","workflow","pipeline"]):
        rec.append("TOOL: mae (mae-master-automation-engine)")
        rec.append("TOOL: tcc (tcc-task-command-center)")
        rec.append("SKILL: all-agents")

    if any(w in task_l for w in ["ads","ppc","google ads","meta","facebook"]):
        rec.append("SKILL: ads-strategy, ads-copy, ads-creative")
        rec.append("TOOL: daily-ads-audit.py")

    if rec:
        print(f"\nBest components for '{task}':")
        for r in rec:
            print(f"  → {r}")
    else:
        print(f"Generic: use mae run \"{task}\" to auto-route")

def wire(a, b):
    """Generate minimal glue between two components."""
    reg = load()
    print(f"\nWiring: {a} ↔ {b}")
    print("""
# AUTO-GENERATED GLUE
import subprocess, json
from pathlib import Path

REGISTRY = Path.home() / ".claude/inventory/registry.json"

def get_component(name):
    with open(REGISTRY) as f:
        reg = json.load(f)
    for category in reg.values():
        if isinstance(category, list):
            for item in category:
                if isinstance(item, dict) and item.get("name","").lower() == name.lower():
                    return item
    return None

comp_a = get_component("{a}")
comp_b = get_component("{b}")

# Wire: pass output of a as input to b
def run_pipeline(input_data):
    # Step 1: run component A
    result_a = subprocess.run(
        ["python3", comp_a.get("path", comp_a["name"])],
        input=json.dumps(input_data), capture_output=True, text=True
    )
    # Step 2: feed into B
    result_b = subprocess.run(
        ["python3", comp_b.get("path", comp_b["name"])],
        input=result_a.stdout, capture_output=True, text=True
    )
    return result_b.stdout
""".format(a=a, b=b))

def status():
    reg = load()
    print(f"\nINVENTORY MESH STATUS  [{reg['updated'][:19]}]")
    print("="*55)
    print(f"  Skills:      {len(reg['skills']):>4}")
    print(f"  Models:      {len(reg['ollama_models']):>4}  {[m['name'] for m in reg['ollama_models']]}")
    print(f"  MCP:         {len(reg['mcp_servers']):>4}  {[m['name'] for m in reg['mcp_servers']]}")
    print(f"  Bin tools:   {len(reg['bin_tools']):>4}")
    print(f"  Repos:       {len(reg['installed_repos']):>4}")
    print(f"  MAE modules: {len(reg['mae_modules']):>4}")
    print(f"  TCC cmds:    {len(reg['tcc_commands']):>4}")
    print(f"  Python pkgs: {len(reg['python_packages']):>4}  {reg['python_packages'][:6]}")
    print(f"  Paperclip:   {reg['paperclip']['status']}")
    print(f"\nLLM Routes:")
    for r in reg.get("llm_routes", []):
        sym = "✓" if r["status"] in ("up","configured") else "✗"
        print(f"    {sym} {r['name']}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "status":
        status()
    elif args[0] == "query" and len(args) > 1:
        query(" ".join(args[1:]))
    elif args[0] == "best" and len(args) > 1:
        best(" ".join(args[1:]))
    elif args[0] == "wire" and len(args) > 2:
        wire(args[1], args[2])
    elif args[0] == "refresh":
        subprocess.run(["python3", str(Path.home() / ".claude/bin/inventory-scan.py")])
        status()
    else:
        print(__doc__)
