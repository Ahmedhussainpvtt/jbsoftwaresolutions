import re
import urllib.request

req = urllib.request.Request(
    "https://ahmedhussainpvtt.github.io/jbsoftwaresolutions-staging/index.html",
    headers={"Cache-Control": "no-cache", "Pragma": "no-cache", "User-Agent": "Mozilla/5.0"},
)
html = urllib.request.urlopen(req).read().decode()
print("scripts", re.findall(r'src="([^"]+)"', html))
print("css", re.findall(r'href="([^"]+\.css)"', html))
print("local dist expects index-BHdM4gnm.js")
