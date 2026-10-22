import base64
import re
import urllib.request

KEY = "6Lf-LsEtAAAAAKGPRWhI5GDDjIYNOa_hWohbAJ9c"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"}

api_js = urllib.request.urlopen(
    urllib.request.Request("https://www.google.com/recaptcha/api.js", headers=UA), timeout=20
).read().decode("utf-8", "ignore")
ver = re.search(r"releases/([^/]+)/", api_js)
v = ver.group(1) if ver else ""


def co_for(origin: str) -> str:
    return base64.b64encode(origin.encode()).decode().rstrip("=").replace("+", "-").replace("/", "_") + "."


for origin in ["https://easypeeze.com:443", "https://jbsoftwaresolutions.com:443"]:
    url = f"https://www.google.com/recaptcha/api2/anchor?ar=1&k={KEY}&co={co_for(origin)}&hl=en&v={v}&size=normal"
    html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20).read().decode("utf-8", "ignore")
    bad = "Invalid domain" in html or "invalid domain" in html.lower()
    print(origin, "| invalid-domain:", bad, "| has token field:", "recaptcha-token" in html)
