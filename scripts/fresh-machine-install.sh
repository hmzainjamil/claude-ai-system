#!/bin/bash
# fresh-machine-install.sh
# One command restores ENTIRE HMZ Claude Code system on any new Mac
# Usage: bash fresh-machine-install.sh

set -e
GITHUB_USER="hmzainjamil"
CLAUDE_DIR="$HOME/.claude"
LOG="$HOME/Downloads/install-log-$(date +%Y%m%d-%H%M%S).txt"

echo "🚀 HMZ Claude AI System — Fresh Machine Install"
echo "================================================"
echo "Logging to: $LOG"

log() { echo "$1" | tee -a "$LOG"; }

# 1. Prerequisites
log "[1/8] Checking prerequisites..."
command -v brew >/dev/null || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
command -v git >/dev/null || brew install git
command -v gh >/dev/null || brew install gh
command -v node >/dev/null || brew install node
command -v python3 >/dev/null || brew install python3
command -v ollama >/dev/null || brew install ollama
log "  ✓ Prerequisites OK"

# 2. GitHub auth
log "[2/8] GitHub auth..."
gh auth status 2>/dev/null || gh auth login
log "  ✓ GitHub authenticated"

# 3. Clone master repo
log "[3/8] Cloning master repo..."
mkdir -p "$CLAUDE_DIR"
if [ -d "$CLAUDE_DIR/.git" ]; then
  git -C "$CLAUDE_DIR" pull origin main
  log "  ✓ Updated existing ~/.claude"
else
  gh repo clone $GITHUB_USER/claude-ai-system "$CLAUDE_DIR/master-backup"
  log "  ✓ Cloned to ~/.claude/master-backup"
fi

# 4. Restore bin scripts
log "[4/8] Restoring bin scripts..."
mkdir -p "$CLAUDE_DIR/bin"
if [ -d "$CLAUDE_DIR/master-backup/bin" ]; then
  cp -r "$CLAUDE_DIR/master-backup/bin/"* "$CLAUDE_DIR/bin/"
  chmod +x "$CLAUDE_DIR/bin/"*
  log "  ✓ $(ls $CLAUDE_DIR/bin | wc -l | tr -d ' ') bin scripts restored"
fi

# 5. Restore skills
log "[5/8] Restoring skills..."
mkdir -p "$CLAUDE_DIR/skills"
if [ -d "$CLAUDE_DIR/master-backup/skills" ]; then
  cp -r "$CLAUDE_DIR/master-backup/skills/"* "$CLAUDE_DIR/skills/"
  log "  ✓ $(ls $CLAUDE_DIR/skills | wc -l | tr -d ' ') skills restored"
fi

# 6. Restore agents
log "[6/8] Restoring agents..."
mkdir -p "$CLAUDE_DIR/agents"
if [ -d "$CLAUDE_DIR/master-backup/agents" ]; then
  cp -r "$CLAUDE_DIR/master-backup/agents/"* "$CLAUDE_DIR/agents/" 2>/dev/null || true
  log "  ✓ agents restored"
fi

# 7. Install daily sync daemon
log "[7/8] Installing daily sync daemon..."
cp "$CLAUDE_DIR/bin/daily-sync-repos.sh" "$CLAUDE_DIR/bin/" 2>/dev/null || true
chmod +x "$CLAUDE_DIR/bin/daily-sync-repos.sh" 2>/dev/null || true

PLIST="$HOME/Library/LaunchAgents/com.hmz.daily-repo-sync.plist"
cat > "$PLIST" << PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.hmz.daily-repo-sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/mc/.claude/bin/daily-sync-repos.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>23</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/daily-repo-sync.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/daily-repo-sync-err.log</string>
    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
PLISTEOF
launchctl load "$PLIST" 2>/dev/null || true
log "  ✓ Daily sync daemon installed (runs 11 PM)"

# 8. Pull Ollama models
log "[8/8] Pulling Ollama models..."
ollama serve &>/dev/null &
sleep 3
ollama pull qwen2.5:7b 2>/dev/null &
log "  ✓ Ollama models queued"

# Done
log ""
log "================================================"
log "✅ INSTALL COMPLETE"
log "  bin scripts: $(ls $CLAUDE_DIR/bin | wc -l | tr -d ' ')"
log "  skills:      $(ls $CLAUDE_DIR/skills | wc -l | tr -d ' ')"
log "  Next: set API keys in ~/.claude/tier0.env"
log "  Log: $LOG"
log "================================================"
