# -*- coding: utf-8 -*-
"""
Master Builder Script for Indigo Books India
Produces:
1. preview.html (100% self-contained, Vanilla HTML/CSS/JS, zero Liquid tags, zero emojis)
2. Native Shopify .liquid sections
3. indigo-books-theme.zip
"""

import os
import re
import subprocess
import zipfile

print("Master Builder Script Initialized.")

