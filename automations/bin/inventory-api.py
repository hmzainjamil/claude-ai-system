#!/usr/bin/env python3
"""
Inventory Mesh HTTP API — runs locally on port 7070
Any agent/n8n workflow hits this to query/register/route inventory.
"""
import subprocess, json
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

MESH     = str(Path.home() / ".claude/bin/inventory-mesh.py")
REG      = str(Path.home() / ".claude/bin/inventory-register.py")
MAE_BIN  = str(Path.home() / "mae-master-automation-engine/mae")
TCC_BIN  = str(Path.home() / "tcc-task-command-center/tcc-dashboard")
ADS_BIN  = str(Path.home() / ".claude/bin/daily-ads-audit.py")
AGENCY_P = str(Path.home() / ".claude/bin/agency-email-pickup")
AGENCY_R = str(Path.home() / ".claude/bin/agency-run")

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, timeout=30,
               env={"HOME": str(Path.home()), "PATH": "/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin"})
    except Exception as e:
        return f"Error: {e}"

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass  # quiet

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}") if length else {}
        action = body.get("action", "status")
        args   = body.get("args", body.get("keyword", body.get("task", "")))

        if action == "query":
            out = run(f'python3 {MESH} query "{args}"')
        elif action == "best":
            out = run(f'python3 {MESH} best "{args}"')
        elif action == "refresh":
            out = run(f'python3 {MESH} refresh')
        elif action == "register":
            t, n, p, d = body.get("type","tool"), body.get("name","?"), body.get("path","/tmp"), body.get("desc","")
            out = run(f'python3 {REG} {t} "{n}" "{p}" "{d}"')
        elif action == "status":
            out = run(f'python3 {MESH} status')
        elif action == "wire":
            a2, b2 = args.split(",") if "," in args else (args, "")
            out = run(f'python3 {MESH} wire "{a2.strip()}" "{b2.strip()}"')
        elif action == "mae-daily":
            mae_out = run(f'{MAE_BIN} daily 2>&1 || echo "mae daily done"')
            tcc_out = run(f'{TCC_BIN} 2>&1 || echo "tcc done"')
            out = f"MAE:\n{mae_out}\n\nTCC:\n{tcc_out}"
        elif action == "ads-audit":
            out = run(f'python3 {ADS_BIN} 2>&1 || echo "audit complete"')
        elif action == "agency-run":
            pickup = run(f'{AGENCY_P} 2>&1 || echo "pickup done"')
            agency = run(f'{AGENCY_R} 2>&1 || echo "agency done"')
            out = f"PICKUP:\n{pickup}\n\nRUN:\n{agency}"
        else:
            out = run(f'python3 {MESH} status')

        resp = json.dumps({"action": action, "output": out, "success": not out.startswith("Error")}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(resp))
        self.end_headers()
        self.wfile.write(resp)

    def do_GET(self):
        out = run(f'python3 {MESH} status')
        resp = json.dumps({"status": "ok", "output": out}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(resp))
        self.end_headers()
        self.wfile.write(resp)

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 7070), Handler)
    print("[inventory-api] Listening on http://localhost:7070")
    server.serve_forever()
