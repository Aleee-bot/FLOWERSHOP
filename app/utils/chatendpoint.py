from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from app.intent.chatservice import handle_user_message

@csrf_exempt
def chat_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    try:
        body = json.loads(request.body)
        user_message = body.get("message", "").strip()

        if not user_message:
            return JsonResponse({"response": "Please ask a question."})

        response_text = handle_user_message(user_message)

        return JsonResponse({"response": response_text})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)