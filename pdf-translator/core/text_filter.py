import re

URL = re.compile(r"https?://|www\.")
DOI = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
EMAIL = re.compile(r"\b[\w.+-]+@[\w.-]+\.\w+\b")
PURE_NUM = re.compile(r"^[\d\s.,+-]+$")


def should_translate(text: str) -> bool:
    t = text.strip()
    if not t:
        return False
    if URL.search(t) or DOI.search(t) or EMAIL.search(t):
        return False
    if PURE_NUM.match(t):
        return False
    if len(t) <= 3 and t.isdigit():
        return False
    return any(c.isalpha() for c in t)
