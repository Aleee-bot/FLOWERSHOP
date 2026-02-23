from app.intent import intentdetect
from app.utils.checkindb import checkindb

def handle_user_message(message: str):
    decision = intentdetect.detect_intent(message)

    if decision["route"] == "DB":
        flower_data = checkindb(decision["flower"])

        if flower_data["status"] == "found":
            if decision["intent"] == "price":
                return f"The price of {flower_data['flower_name']} is ${flower_data['flower_price']}."


            if decision["intent"] == "quantity":
                return f"We currently have {flower_data['flower_quantity']} {flower_data['flower_name']}s in stock."

            return f"{flower_data['flower_name']} is available."

        return "Sorry, we don't have that flower."

    # LLM fallback (later)
    return "I'm happy to help! Could you please be more specific?"