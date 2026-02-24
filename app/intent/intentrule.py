from app.models import Flower

DB_INTENT_KEYWORDS = {
    "price": ["price", "cost", "rate", "how much"],
    "quantity": ["quantity", "stock", "available", "left", "how many"],
    "availability": ["have", "available", "in stock"],
    "list" : ["list", "show", "available flowers", "flowers" , "flower"]
}

def get_flower():
    return list(Flower.objects.values_list("flower_name", flat = True))