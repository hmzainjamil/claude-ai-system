#!/bin/bash
# Starts cloudflared quick tunnel to localhost:7070
# Captures public URL and writes to ~/.claude/inventory/tunnel-url.txt

URL_FILE="$HOME/.claude/inventory/tunnel-url.txt"
LOG="$HOME/.claude/inventory/tunnel.log"

mkdir -p "$HOME/.claude/inventory"

# Kill any old instance
pkill -f "cloudflared tunnel --url" 2>/dev/null
sleep 1

# Start tunnel, capture URL from stderr
cloudflared tunnel --url http://localhost:7070 2>&1 | while IFS= read -r line; do
    echo "$line" >> "$LOG"
    if echo "$line" | grep -q "trycloudflare.com"; then
        url=$(echo "$line" | grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com')
        if [ -n "$url" ]; then
            echo "$url" > "$URL_FILE"
            echo "[tunnel] URL: $url" >> "$LOG"
            echo "[tunnel] Written to $URL_FILE"
            # Update all n8n cloud workflows with new URL
            python3 "$HOME/.claude/bin/tunnel-sync-n8n.py" >> "$LOG" 2>&1 &
        fi
    fi
done
