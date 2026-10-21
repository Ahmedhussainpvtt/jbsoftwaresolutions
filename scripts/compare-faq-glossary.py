import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(r"c:/Users/Alex/OneDrive/Desktop/ExpenseTracker/jbsoftwaresolutions-staging/src/data")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


stg = json.loads(ROOT.joinpath("faqTopics.js").read_text(encoding="utf-8").split("export default ", 1)[1])
gloss = json.loads(ROOT.joinpath("glossaryTerms.js").read_text(encoding="utf-8").split("export default ", 1)[1])

prod_faq = fetch("https://jbsoftwaresolutions.com/faq/")
prod_gloss = fetch("https://jbsoftwaresolutions.com/glossary/")
prod_topic = fetch("https://jbsoftwaresolutions.com/faq/website-development-cost-india/")
prod_term = fetch("https://jbsoftwaresolutions.com/glossary/seo/")

prod_faq_cards = len(re.findall(r'class="faq-topic-card', prod_faq))
prod_gloss_cards = len(re.findall(r'class="term-card', prod_gloss))
prod_details = len(re.findall(r"<details>", prod_topic))
prod_term_h1 = re.search(r"<h1>([^<]+)</h1>", prod_term).group(1)

print("PROD faq cards", prod_faq_cards, "STG", stg["topicCount"], "OK", prod_faq_cards == stg["topicCount"])
print("PROD gloss cards", prod_gloss_cards, "STG", len(gloss), "OK", prod_gloss_cards == len(gloss))
print("PROD topic Qs", prod_details, "STG", len(stg["topics"][0]["qs"]), "OK", prod_details == len(stg["topics"][0]["qs"]))
print("PROD term h1", prod_term_h1)
print("STG qs total", stg["count"])
