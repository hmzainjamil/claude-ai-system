#!/usr/bin/env python3
"""
Citability Scorer — Analyzes content blocks for AI citation readiness.
Scores passages based on how likely AI models are to cite them.

Based on research showing optimal AI-cited passages are:
- 134-167 words long
- Self-contained (extractable without context)
- Fact-rich with specific statistics
- Structured with clear answer patterns
"""

import sys
import json
import re
from typing import Optional

try:
    import requests
    from bs4 import BeautifulSoup
except Im