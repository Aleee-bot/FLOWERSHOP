from app.models import Flower

def checkindb(flower_name : str ):
    flower_name = flower_name.strip()
    flower = Flower.objects.filter(flower_name__iexact=flower_name).first()

    if not flower:
        return {
            "status": "not found" , 
            "message": f"Flower with name '{flower_name}' not found in the database."
        }
    
    return {
        "status": "found",
        "flower_name": flower.flower_name,
        "flower_quantity": flower.flower_quantity,
        "flower_price": flower.flower_price
    }