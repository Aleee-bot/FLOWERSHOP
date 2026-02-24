from app.intent import intentdetect
from app.utils.checkindb import checkindb
from app.utils.llm import call_llm  
from app.models import Flower

def handle_user_message(message: str):
    decision = intentdetect.detect_intent(message)

    if decision["route"] == "DB":

        if decision["intent"] == "list":
            flowers = Flower.objects.all()

            if not flowers.exists():
                return "Sorry, we currently have no flowers in stock."

            response = "We currently have:\n"
            for f in flowers:
                response += f"- {f.flower_name}\n"

            return response.strip()

        flower_data = checkindb(decision["flower"])

        if flower_data["status"] == "found":
            if decision["intent"] == "price":
                return f"The price of {flower_data['flower_name']} is Rs.{flower_data['flower_price']}."

            if decision["intent"] == "quantity":
                return f"We currently have {flower_data['flower_quantity']} {flower_data['flower_name']}s in stock."

            return f"{flower_data['flower_name']} is available."

        return "Sorry, we don't have that flower."

    elif decision["route"] == "NOT_FOUND":
        flower = decision.get("flower", "that flower")
        return f"Sorry, {flower} is out of stock."

    return call_llm(message)