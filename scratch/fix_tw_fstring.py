with open('build_html_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """  <!-- Tailwind CSS Engine -->
  <script>
    (function(){
      var _w = console.warn;
      console.warn = function() {
        if (arguments[0] && typeof arguments[0] === 'string' && arguments[0].indexOf('cdn.tailwindcss.com') !== -1) return;
        _w.apply(console, arguments);
      };
    })();
  </script>
  <script src="https://cdn.tailwindcss.com"></script>"""

replacement = """  <!-- Tailwind CSS Engine -->
  <script src="https://cdn.tailwindcss.com"></script>"""

assert target in text, "Target not found"
text = text.replace(target, replacement, 1)

with open('build_html_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed build_html_generator.py f-string syntax!")
