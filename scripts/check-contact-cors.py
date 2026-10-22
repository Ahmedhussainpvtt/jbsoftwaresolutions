import json
import urllib.request

API = "https://easypeeze-tools-j6dbitzprq-el.a.run.app"


def preflight(path: str, origin: str) -> str:
    req = urllib.request.Request(
        API + path,
        method="OPTIONS",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.headers.get("Access-Control-Allow-Origin") or "-"


with urllib.request.urlopen(API + "/health", timeout=20) as r:
    h = json.loads(r.read())
print("health ok:", h.get("ok"), "| authV2Required:", h.get("authV2Required"), "| pepper:", h.get("pepperConfigured"))

for path, origin in [
    ("/contact", "https://jbsoftwaresolutions.com"),
    ("/contact", "https://easypeeze.com"),
    ("/admin/login", "https://jbsoftwaresolutions.com"),
    ("/create-order", "https://jbsoftwaresolutions.com"),
]:
    print(f"{path:14} from {origin:34} -> allow-origin: {preflight(path, origin)}")
