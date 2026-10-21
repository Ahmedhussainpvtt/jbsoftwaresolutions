import re
import urllib.request

req = urllib.request.Request(
    "https://jbsoftwaresolutions.com/?r=react2",
    headers={"Cache-Control": "no-cache", "User-Agent": "Mozilla/5.0"},
)
with urllib.request.urlopen(req, timeout=30) as r:
    html = r.read().decode("utf-8", "ignore")

robots = re.search(r'name="robots" content="([^"]+)"', html)
print("robots", robots.group(1) if robots else None)
print("js", re.findall(r'src="(/assets/[^"]+)"', html))
print("css", re.findall(r'href="(/assets/[^"]+\.css)"', html))
print("has root", 'id="root"' in html)
print("old main.js", "main.js" in html)
print("vite chunk", "index-DdcUMtrq" in html or "index-" in html)
