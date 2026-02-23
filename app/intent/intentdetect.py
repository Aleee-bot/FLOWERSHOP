from app.utils.checkindb import checkindb
from app.intent.intentrule import DB_INTENT_KEYWORDS, FLOWER_KEYWORDS
import re

def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    return text

def detect_intent(user_input: str):
    text = normalize_text(user_input)

    # Check if user is asking about flowers
    flower_found = None
    for flower in FLOWER_KEYWORDS:
        if flower in text:
            flower_found = flower
            break

    if not flower_found:
        return {
            "route": "LLM",
            "reason": "No flower mentioned"
        }

    # Check DB-related keywords
    for intent, keywords in DB_INTENT_KEYWORDS.items():
        for word in keywords:
            if word in text:
                return {
                    "route": "DB",
                    "intent": intent,
                    "flower": flower_found
                }

    return {
        "route": "LLM",
        "reason": "Non-DB question"
    }