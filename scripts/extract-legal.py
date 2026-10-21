from pathlib import Path
import re
import json

base = Path(r"c:\Users\Alex\OneDrive\Desktop\ExpenseTracker\JB Software Solutions")
out = Path(r"c:\Users\Alex\OneDrive\Desktop\ExpenseTracker\jbsoftwaresolutions-staging\src\data")
out.mkdir(parents=True, exist_ok=True)


def extract_main(name: str) -> str:
    html = (base / name / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<main>(.*?)</main>", html, re.S)
    body = m.group(1).strip()
    repl = {
        'href="../contact/"': 'data-to="/contact"',
        'href="../privacy/"': 'data-to="/privacy"',
        'href="../terms/"': 'data-to="/terms"',
        'href="../pricing/"': 'data-to="/pricing"',
        'href="../about/"': 'data-to="/about"',
        'href="../faq/"': 'data-to="/faq"',
        'href="../blog/"': 'data-to="/blog"',
        'href="../glossary/"': 'data-to="/glossary"',
        'href="../"': 'data-to="/"',
    }
    for a, b in repl.items():
        body = body.replace(a, b)
    body = re.sub(r'href="\.\./services/([^"]+)/"', r'data-to="/services/\1"', body)
    body = body.replace(" btn-magnet", "")
    body = body.replace(' class="reveal"', "")
    return body


for name in ("privacy", "terms"):
    body = extract_main(name)
    (out / f"{name}Html.js").write_text(
        "export default " + json.dumps(body) + "\n", encoding="utf-8"
    )
    print(name, "ok", len(body))
