import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
    You are a helpful assistant for a flower shop.
    The database handles prices and stock.
    If the user asks something general, care tips, answer politely and briefly.
    Do NOT hallucinate prices or availability.
    """
)

def call_llm(user_message: str) -> str:
    """
    Gemini LLM fallback for non-database questions
    """
    try:
        response = model.generate_content(
            user_message,
            generation_config={
                "temperature": 0.4,
                "max_output_tokens": 150
            }
        )

        return response.text.strip()

    except Exception as e:
        return "Sorry, I'm having trouble answering that right now."