#!/bin/bash
# INVENTORY WATCHER — auto-re-scans when new tools/skills/repos land
# LaunchAgent runs this; uses fswatch if available, else polls every 5min

SCAN="python3 $HOME/.claude/bin/inventory-scan.py"
WATCH_DIRS=(
  "$HOME/.claude/skills"
  "$HOME/.claude/bin"
  "$HOME/installed-repos"
  "$HOME/mae-master-automation-engine"
  "$HOME/tcc-task-command-center"
  "$HOME/.mcp.json"
)

echo "[inventory-watch] Starting..."

if command -v fswatch &>/dev/null; then
  echo "[inventory-watch] Using fswatch (event-driven)"
  fswatch -o "${WATCH_DIRS[@]}" 2>/dev/null | while read count; do
    echo "[inventory-watch] Change detected — rescanning..."
    $SCAN
  done
else
  echo "[inventory-watch] fswatch not found — polling every 5min"
  while true; do
    $SCAN > /dev/null 2>&1
    sleep 300
  done
fi
