import subprocess, time

html_content = """<!DOCTYPE html>
<html>
<head><title>Test Cover</title></head>
<body>
<h1>Testing Cover Image</h1>
<img id="testImg" src="https://images.rajkamalprakashan.com/products/2026/10/17/7a36eca7-531b-428e-b957-84004ec4b419-jag-piyari-ab-ka-sove-hb-front.jpg" alt="test" width="300" />
<script>
  const img = document.getElementById('testImg');
  img.onload = () => console.log('IMG LOADED SUCCESS');
  img.onerror = (e) => console.log('IMG LOAD ERROR', e);
</script>
</body>
</html>"""

with open('scratch/test_cover_load.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created scratch/test_cover_load.html")
