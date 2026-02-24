from app.intent.intentrule import DB_INTENT_KEYWORDS, get_flower
import re

def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return text

def detect_intent(user_input: str):
    text = normalize_text(user_input)

    for word in DB_INTENT_KEYWORDS.get("list", []):
        if word in text:
            return {
                "route": "DB",
                "intent": "list"
            }

    db_flowers = [f.lower() for f in get_flower()]
    flower_found = None

    for flower in db_flowers:
        if flower in text:
            flower_found = flower
            break

    if flower_found:
        for intent, keywords in DB_INTENT_KEYWORDS.items():
            if intent == "list":
                continue
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

    words = text.split()
    possible_flower = words[-1] if words else None

    return {
        "route": "NOT_FOUND",
        "flower": possible_flower
    }