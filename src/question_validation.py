import os
from dotenv import load_dotenv
import google.generativeai as genai

PROMPT = "Provided is a messy transcription of a conversation. Your job is to decipher if a student asked a question. Realize there may be no clear end to the question, as our speech to text is poor. Say yes or no"

load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 16,
        "response_mime_type": "text/plain",
    },
)

chat_session = model.start_chat()

def validate_question(transcription):
    if transcription == "":
        return False

    response = chat_session.send_message(f"{PROMPT}\nTranscription: {transcription}")
    print(f'Response: {response.text.strip().lower()}\n')
    return response.text.strip().lower() == "yes"
