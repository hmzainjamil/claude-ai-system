#!/usr/bin/env python3
"""
Reads current tunnel URL from ~/.claude/inventory/tunnel-url.txt
Updates ~/.claude/inventory/current-tunnel-url for reference.
The actual n8n workflow updates are handled by the LaunchAgent restart
triggering tunnel-start.sh which fires this script.

Since we can't call n8n REST API directly (JWT is MCP-only),
this writes the new URL to a known location. Workflows use neverError=true
so they gracefully fail when laptop is off.
"""
from pathlib import Path
from datetime import datetime

URL_FILE  = Path.home() / ".claude/inventory/tunnel-url.txt"
STAMP     = Path.home() / ".claude/inventory/tunnel-status.json"

def main():
    if not URL_FILE.exists():
        print("No tunnel URL file.")
        return

    url = URL_FILE.read_text().strip()
    print(f"[tunnel-sync] Current URL: {url}")

    import json
    status = {
        "tunnel_url": url,
        "updated_at": datetime.now().isoformat(),
        "note": "n8n workflows updated manually via MCP to use this URL. Re-run tunnel-sync after URL change."
    }
    STAMP.write_text(json.dumps(status, indent=2))
    print(f"[tunnel-sync] Status written to {STAMP}")

if __name__ == "__main__":
    main()
