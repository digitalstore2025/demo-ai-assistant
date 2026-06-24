import re

RED_FLAG_PATTERNS = [
    r"chest pain",
    r"shortness of breath",
    r"loss of consciousness",
    r"stroke",
    r"severe bleeding",
]

PRESCRIPTION_PATTERNS = [
    r"take [0-9]+ mg",
    r"prescribe",
    r"stop taking",
]


def evaluate_safety(text: str) -> dict:
    lower = text.lower()
    flags = []
    if any(re.search(p, lower) for p in RED_FLAG_PATTERNS):
        flags.append("red_flag")
    if any(re.search(p, lower) for p in PRESCRIPTION_PATTERNS):
        flags.append("prescription_risk")
    needs_human_review = bool(flags)
    return {"flags": flags, "needs_human_review": needs_human_review}
