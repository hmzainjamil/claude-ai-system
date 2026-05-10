#!/usr/bin/env python3
"""
llms.txt Generator — Creates and validates llms.txt files for AI crawler guidance.

The llms.txt standard is an emerging specification that helps AI crawlers
understand your site structure and find your most important content.

Location: /llms.txt (root of domain)
Extended: /llms-full.txt (detailed version)
"""

import sys
import json
import re
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
   