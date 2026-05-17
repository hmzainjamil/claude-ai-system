#!/bin/bash
# daily-sync-repos.sh
# Runs 11 PM daily — syncs ALL local work into master repo + creates new repos for new files
# LaunchAgent: com.hmz.daily-repo-sync

MASTER="$HOME/claude-ai-system"
CLAUDE_DIR="$HOME/.claude"
GIT_EMAIL="hmzainjamil@gmail.com"
GIT_NAME="hmzainjamil"
LOG="/tmp/daily-repo-sync.log"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M:%S)

log() { echo "[$TIME] $1" | tee -a "$LOG"; }

log "===== DAILY SYNC START [$DATE] ====="

# ── 1. Sync ~/.claude/bin → master/bin ──────────────────────────────────────
log "[1] Syncing bin scripts..."
NEW_BIN=0
for f in "$CLAUDE_DIR/bin/"*; do
  fname=$(basename "$f")
  dest="$MASTER/bin/$fname"
  # Skip directories
  [ -f "$f" ] || continue
  # Copy if missing or newer
  if [ ! -f "$dest" ] || [ "$f" -nt "$dest" ]; then
    cp "$f" "$dest"
    chmod +x "$dest"
    NEW_BIN=$((NEW_BIN + 1))
    log "  + bin: $fname"
  fi
done
log "  ✓ $NEW_BIN new/updated bin files"

# ── 2. Sync ~/.claude/skills → master/skills ────────────────────────────────
log "[2] Syncing skills..."
NEW_SKILLS=0
for d in "$CLAUDE_DIR/skills/"/*/; do
  skill=$(basename "$d")
  dest="$MASTER/skills/$skill"
  if [ ! -d "$dest" ]; then
    cp -r "$d" "$dest"
    NEW_SKILLS=$((NEW_SKILLS + 1))
    log "  + skill: $skill"
  elif [ -f "$d/SKILL.md" ] && [ "$d/SKILL.md" -nt "$dest/SKILL.md" ]; then
    cp -r "$d" "$dest"
    NEW_SKILLS=$((NEW_SKILLS + 1))
    log "  ~ skill updated: $skill"
  fi
done
log "  ✓ $NEW_SKILLS new/updated skills"

# ── 3. Sync ~/.claude/agents → master/agents ────────────────────────────────
log "[3] Syncing agents..."
if [ -d "$CLAUDE_DIR/agents" ]; then
  rsync -aq "$CLAUDE_DIR/agents/" "$MASTER/agents/" 2>/dev/null || true
  log "  ✓ agents synced"
fi

# ── 4. Update repos manifest ─────────────────────────────────────────────────
log "[4] Updating repos manifest..."
ALL_REPOS=$(gh repo list hmzainjamil --limit 100 --json name,description,updatedAt \
  2>/dev/null | python3 -c "
import sys, json
repos = json.load(sys.stdin)
print(f'# HMZ All Repos — {len(repos)} total')
print(f'Last updated: $(date)')
print()
print('| Repo | Description | Clone |')
print('|---|---|---|')
for r in sorted(repos, key=lambda x: x['name']):
    name = r['name']
    desc = r.get('description','') or ''
    print(f'| [{name}](https://github.com/hmzainjamil/{name}) | {desc[:60]} | \`gh repo clone hmzainjamil/{name}\` |')
" 2>/dev/null)

if [ -n "$ALL_REPOS" ]; then
  echo "$ALL_REPOS" > "$MASTER/repos/REPOS_MANIFEST.md"
  log "  ✓ Manifest updated"
fi

# ── 5. Detect new local dirs that need GitHub repos ──────────────────────────
log "[5] Detecting new work needing repos..."
EXISTING_REPOS=$(gh repo list hmzainjamil --limit 100 --json name | python3 -c "import sys,json; [print(r['name']) for r in json.load(sys.stdin)]" 2>/dev/null)

for dir in "$HOME"/*/; do
  dirname=$(basename "$dir")
  # Skip system dirs
  [[ "$dirname" == "Library" || "$dirname" == "Applications" || "$dirname" == "Desktop" ]] && continue
  [[ "$dirname" == "Documents" || "$dirname" == "Downloads" || "$dirname" == "Movies" ]] && continue
  [[ "$dirname" == "Music" || "$dirname" == "Pictures" || "$dirname" == "Public" ]] && continue
  [[ "$dirname" == "claude-ai-system" ]] && continue

  # Check if it has a README and no remote repo
  if [ -f "$dir/README.md" ] && ! echo "$EXISTING_REPOS" | grep -q "^${dirname}$"; then
    log "  NEW REPO NEEDED: $dirname — creating..."
    cd "$dir"
    git init -q 2>/dev/null || true
    git checkout -b main -q 2>/dev/null || true
    git config user.email "$GIT_EMAIL"
    git config user.name "$GIT_NAME"

    DESC=$(head -3 README.md | grep -v "^#" | head -1 | tr -d '\n' | cut -c1-100)
    gh repo create "hmzainjamil/$dirname" --public --description "$DESC" 2>/dev/null || true
    git add -A
    git commit -qm "feat: auto-sync $(date +%Y-%m-%d)" 2>/dev/null || true
    git remote remove origin 2>/dev/null || true
    git remote add origin "https://github.com/hmzainjamil/$dirname.git"
    git push -u origin main -q 2>/dev/null && log "    ✓ Pushed: $dirname" || log "    ✗ Push failed: $dirname"
    cd ~
  fi
done

# ── 6. Commit + push master repo ─────────────────────────────────────────────
log "[6] Committing master repo..."
cd "$MASTER"
git config user.email "$GIT_EMAIL"
git config user.name "$GIT_NAME"
git add -A

CHANGES=$(git status --porcelain | wc -l | tr -d ' ')
if [ "$CHANGES" -gt 0 ]; then
  git commit -qm "auto: daily sync $DATE — $CHANGES files updated"
  git push -q origin main && log "  ✓ Master repo pushed ($CHANGES changes)"
else
  log "  ✓ Master repo already up to date"
fi

log "===== DAILY SYNC COMPLETE [$DATE $TIME] ====="
log ""
