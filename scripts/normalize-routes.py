from pathlib import Path
import re

files = [
    Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/jbsoftwaresolutions-staging/src/pages/Home.jsx"),
    Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/jbsoftwaresolutions-staging/src/pages/ServicePage.jsx"),
    Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/jbsoftwaresolutions-staging/src/data/site.js"),
]

for p in files:
    t = p.read_text(encoding="utf-8")
    t = (
        t.replace("/contact/", "/contact")
        .replace("/pricing/", "/pricing")
        .replace("/faq/", "/faq")
        .replace("/blog/", "/blog")
        .replace("/glossary/", "/glossary")
    )
    t = re.sub(r"/services/([a-z0-9-]+)/", r"/services/\1", t)
    p.write_text(t, encoding="utf-8")
    print(p.name, "ok")
