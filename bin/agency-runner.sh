#!/bin/bash
# Agency Daily Runner — caffeinate keeps machine awake for 90 min
source "$HOME/.claude/tier0.env" 2>/dev/null
/usr/bin/caffeinate -i -t 5400 &
CAF_PID=$!
/usr/bin/python3 "$HOME/.claude/bin/agency-run" 2>&1
kill $CAF_PID 2>/dev/null
