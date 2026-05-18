#!/usr/bin/env python3
"""
GitHub Daily Sync — auto-upload new ~/installed-repos to hmzainjamil GitHub.
Runs daily via n8n or LaunchAgent. Skips already-uploaded repos.
"""

import subprocess
import os
import json
import sys
from pathlib import Path
from datetime import datetime

INSTALLED = Path.home() / "installed-repos"
LOG = Path.home() / ".claude/logs/github-sync.log"
STATE = Path.home() / ".claude/logs/github-sync-state.json"
GITHUB_USER = "hmzainjamil"

# Repos to SKIP — clones of external repos (not HMZ's own work)
SKIP_LIST = {
    "microsoft", "apify-org", "ollama", "Fabric", "AGENT-ZERO",
    "500-AI-Agents-Projects", "GPTs", "ShaikhWarsi", "LTX-Video",
    "Hermes-Function-Calling", "JDeepSeek", "DeepSeek-R1", "Ling",
    "llama2.c64", "Proxima", "agentscope", "agentapi", "agentmemory",
    "agent-twitter-client", "agent-browser", "agent-orchestrator",
    "agent-skills", "ai", "ai-ads-claude", "ai-agency-claude",
    "ai-design-team", "ai-elements", "ai-engineering-from-scratch",
    "ai-marketing-claude", "ai-sdk-provider", "ai-website-cloner-template",
    "ai_computer_use", "airllm", "airtable-py-pcorpet", "airtable.js",
    "all_requirements.txt", "amplifying-ai-awesome-generative-engine-optimization",
    "answer-engine-aeo", "anthropic-claude-code-plugins", "anthropic-sdk-go",
    "anthropic-skills", "apify-actor-llmstxt-generator", "apify-agent-skills",
    "apify-mcp-server", "autoresearch", "autoresearch-local-llm", "avatar",
    "awesome-agent-skills", "awesome-agentic-patterns", "awesome-ai-apps",
    "awesome-claude", "awesome-claude-agents", "awesome-claude-code",
    "awesome-claude-code-toolkit", "awesome-claude-plugins", "awesome-claude-skills",
    "awesome-devops-mcp-servers", "awesome-gemini-for-google-cloud",
    "awesome-mcp-servers", "awesome-openclaw", "awesome-openclaw-skills",
    "awesome-openrouter", "awesome-web-scraping", "blink", "cc-copilot-bridge",
    "chatbot", "claude-code", "claude-code-best-practice", "claude-code-plugins",
    "claude-code-plugins-marketplace", "claude-code-plugins-plus",
    "claude-code-security-review-main", "claude-code-templates",
    "claude-code-ultimate-guide", "claude-code-ultimate-guide-landing",
    "claude-cowork-guide", "claude-cowork-guide-landing", "claude-dashboard-trmnl",
    "claude-design-auditor-skill", "claude-mem-main", "claude-office-skills",
    "claude-scientific-skills", "claude-seo", "claude-skills", "claude-task-master",
    "claude-token-efficient", "claudecode.nvim", "claw-code", "cli", "composio",
    "composio-awesome-claude-skills", "composio-openclaw", "computesdk",
    "deepseek-v3", "deer-flow", "dengineproblem-agents", "design-md",
    "everything-claude-code", "free-ai-tools", "frontend-design",
    "geo-seo-claude", "github-mcp-server", "graphify", "hermes-agent",
    "hermes-agent-self-evolution", "hyper", "izak-fisher-generative-engine-optimization-tools",
    "knowledge-work-plugins", "llm-agents-bundle", "llm_council_skill",
    "marketing-skills", "marketingskills", "marketplace-aeorank-aeo-scanner",
    "mattpocock-skills", "mcp-cli", "memvid-main", "n-autoresearch",
    "ngmisl-llmstxt", "obsidian-skills-main", "openclaw", "openclaw-skills-official",
    "openclawd", "opencli", "opencli-1.7.18", "opencli-extension", "opencode",
    "openrouter_api", "paperclip", "playwright-mcp-main", "pro-workflow",
    "pyairtable", "realtime", "rtk-master", "sccache", "skills-main",
    "subconscious-systems-AEO", "subconscious-systems-ollama-subc",
    "supabase-flutter", "supabase-grafana", "supabase-js", "supabase-swift",
    "superpowers-main", "ui-ux-design-pro-skill-main", "ui-ux-pro-max-skill-main",
    "vercel", "vercel-labs-skills", "website-builder-setup", "workflow",
    "ai-search-guru-getcito", "AI-Trader", "Auto-claude-code-research-in-sleep",
    "Awesome-Agent-Memory-main", "Awesome-Collection-Token-Reduction-main",
    "Ethirio-AEO-Generator", "How-to-Clone-Website---Claude-Skills", "MiroFish",
    "Personal_AI_Infrastructure", "addyosmani-agent-engineer",
    "addyosmani-agentic-seo", "addyosmani-web-quality-skills",
    "agentsmd-agents.md", "agency-agents", "anyclaude", "GPTs", "ShaikhWarsi",
    "n8n-resources", "n8nworkflows.xyz",
}

# HMZ's OWN repos — always upload these
OWN_REPOS = {
    "digiminds-speckit", "fact-check-skill", "claude-watch",
    "hermes-paperclip-adapter",
}

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")

def run(cmd, cwd=None, check=True):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if check and r.returncode != 0:
        raise RuntimeError(f"CMD FAILED: {cmd}\n{r.stderr}")
    return r.stdout.strip()

def get_existing_repos():
    out = run(f"gh repo list {GITHUB_USER} --limit 200 --json name -q '.[].name'")
    return set(out.splitlines())

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"uploaded": [], "skipped": [], "last_run": None}

def save_state(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2))

def get_description(name):
    descs = {
        "fact-check-skill": "HMZ Fact-Check AI — 11-step SIFT+CRAAP pipeline, HTML cards, prebunking, misinformation detection",
        "claude-watch": "Claude session watcher — monitors active Claude Code sessions, usage tracking, cost alerts",
        "hermes-paperclip-adapter": "Wire Hermes NousResearch agent as Paperclip AI employee — auto-executes goals, budget-aware",
        "digiminds-speckit": "DigiMinds SpecKit — 6-step SDD generator for DigiMinds agency AI workflows",
    }
    return descs.get(name, f"HMZ AI System — {name} (Hafiz Muhammad Zulqarnain)")

def init_git_and_push(repo_path, repo_name, description):
    """Init git, create GitHub repo, push."""
    # Init git if needed
    if not (repo_path / ".git").exists():
        run("git init", cwd=repo_path)
        run("git add -A", cwd=repo_path)
        try:
            run('git commit -m "Initial commit — HMZ AI System"', cwd=repo_path)
        except Exception:
            pass  # nothing to commit

    # Create GitHub repo
    run(f'gh repo create {GITHUB_USER}/{repo_name} --public --description "{description}" --source=. --push',
        cwd=repo_path)
    log(f"✅ UPLOADED: {repo_name}")
    return True

def sync_existing(repo_path, repo_name):
    """Push latest changes to existing GitHub repo."""
    try:
        remote = run("git remote get-url origin", cwd=repo_path, check=False)
        if not remote:
            run(f"git remote add origin https://github.com/{GITHUB_USER}/{repo_name}.git",
                cwd=repo_path)
        run("git add -A", cwd=repo_path)
        result = run('git diff --cached --quiet', cwd=repo_path, check=False)
        if result == "":
            return False  # no changes
        run(f'git commit -m "Auto-sync {datetime.now().strftime("%Y-%m-%d")}"', cwd=repo_path)
        run("git push origin main --force-with-lease 2>/dev/null || git push origin master --force-with-lease 2>/dev/null || true",
            cwd=repo_path)
        log(f"🔄 SYNCED: {repo_name}")
        return True
    except Exception as e:
        log(f"⚠️  SYNC FAILED: {repo_name} — {e}")
        return False

def main(dry_run=False):
    log("=== GitHub Daily Sync START ===")
    state = load_state()
    existing_gh = get_existing_repos()
    log(f"GitHub repos: {len(existing_gh)} | Installed repos: {len(list(INSTALLED.iterdir()))}")

    uploaded = []
    synced = []
    skipped = []

    for repo_path in sorted(INSTALLED.iterdir()):
        if not repo_path.is_dir():
            continue
        name = repo_path.name

        # Determine if this is HMZ's own work
        is_own = name in OWN_REPOS
        is_external = name in SKIP_LIST

        if is_external and not is_own:
            continue  # skip clones

        # Map local name → GitHub repo name
        gh_name = name.lower().replace("_", "-").replace(" ", "-")

        if gh_name in existing_gh or name in existing_gh:
            # Already on GitHub — sync changes
            if (repo_path / ".git").exists():
                if not dry_run:
                    changed = sync_existing(repo_path, gh_name)
                    if changed:
                        synced.append(name)
        else:
            # New repo — upload
            log(f"NEW: {name} → uploading...")
            if not dry_run:
                try:
                    desc = get_description(name)
                    init_git_and_push(repo_path, gh_name, desc)
                    uploaded.append(name)
                except Exception as e:
                    log(f"❌ FAILED: {name} — {e}")

    state["uploaded"].extend(uploaded)
    state["last_run"] = datetime.now().isoformat()
    save_state(state)

    log(f"=== DONE | Uploaded: {len(uploaded)} | Synced: {len(synced)} ===")
    return {"uploaded": uploaded, "synced": synced}

if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    result = main(dry_run=dry)
    print(json.dumps(result))
