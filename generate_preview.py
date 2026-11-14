# -*- coding: utf-8 -*-
"""
generate_preview.py
Generates the authoritative preview.html using build_preview_html()
"""
import os
from build_html_generator import build_preview_html

def main():
    print("Generating preview.html from build_html_generator.py...")
    html_content = build_preview_html()
    
    with open("preview.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    size_kb = os.path.getsize("preview.html") / 1024
    print(f"preview.html successfully generated! Size: {size_kb:.2f} KB")

if __name__ == "__main__":
    main()

