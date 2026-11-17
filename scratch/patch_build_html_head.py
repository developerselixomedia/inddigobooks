with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = """  <!-- Tailwind CSS Engine -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
{UNIFIED_STORE_CSS}
  </style>
  <script>
    (function() {{
      var origWarn = console.warn;
      console.warn = function() {{
        if (arguments[0] && typeof arguments[0] === 'string' && arguments[0].indexOf('cdn.tailwindcss.com') !== -1) return;
        return origWarn.apply(console, arguments);
      }};
    }})();"""

replacement = """  <!-- Suppress Tailwind Production Warning BEFORE CDN Script Evaluation -->
  <script>
    (function() {{
      var origWarn = console.warn;
      console.warn = function() {{
        if (arguments[0] && typeof arguments[0] === 'string' && arguments[0].indexOf('cdn.tailwindcss.com') !== -1) return;
        return origWarn.apply(console, arguments);
      }};
    }})();
  </script>

  <!-- Tailwind CSS Engine -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
{UNIFIED_STORE_CSS}
  </style>
  <script>"""

assert target in content, "target not found in build_html_generator.py!"
content = content.replace(target, replacement, 1)

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated build_html_generator.py head scripts!")
