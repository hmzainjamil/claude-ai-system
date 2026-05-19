#!/usr/bin/env python3
"""
Called by any installer/skill-creator/tool-builder to register a new component.
Usage: inventory-register.py <type> <name> <path> [description]

Types: skill | tool | model | repo | mcp | agent
"""
import json, sys
from pathlib import Path
from datetime import datetime

REGISTRY = Path.home() / ".claude" / "inventory" / "registry.json"
REGISTRY.parent.mkdir(parents=True, exist_ok=True)

def register(comp_type, name, path, desc=""):
    reg = {}
    if REGISTRY.exists():
        with open(REGISTRY) as f:
            reg = json.load(f)

    # Map type to exact registry key used by scanner
    key_map = {"skill": "skills", "tool": "bin_tools", "model": "ollama_models",
               "repo": "installed_repos", "mcp": "mcp_servers", "agent": "agents"}
    key = key_map.get(comp_type, f"{comp_type}s")
    if key not in reg:
        reg[key] = []

    # Deduplicate by name
    reg[key] = [x for x in reg[key] if x.get("name") != name]
    reg[key].append({"name": name, "path": path, "desc": desc,
                     "registered": datetime.now().isoformat()})
    reg["updated"] = datetime.now().isoformat()

    with open(REGISTRY, "w") as f:
        json.dump(reg, f, indent=2)

    print(f"[inventory] Registered [{comp_type}] {name}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: inventory-register.py <type> <name> <path> [desc]")
        sys.exit(1)
    comp_type, name, path = sys.argv[1], sys.argv[2], sys.argv[3]
    desc = sys.argv[4] if len(sys.argv) > 4 else ""
    register(comp_type, name, path, desc)
