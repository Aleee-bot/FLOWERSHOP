from app.intent.intentrule import DB_INTENT_KEYWORDS, FLOWER_KEYWORDS
import re
from app.models import Flower

def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)  
    return text

def detect_intent(user_input: str):
    text = normalize_text(user_input)

    flowers = Flower.objects.values_list('flower_name', flat=True)

    flower_found = None
    for flower in flowers:
        if flower.lower() in text:
            flower_found = flower
            break

    if not flower_found:
        return {
            "route": "LLM",
            "reason": "No flower mentioned"
        }

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