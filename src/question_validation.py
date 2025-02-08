import os
from dotenv import load_dotenv
import google.generativeai as genai

PROMPT = "Based off the student's question and the professor's response, is the student's question reasonable for credit regardless of accuracy? Answer yes or no"

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

def is_question_reasonable(student_question, professor_response):
    response = chat_session.send_message(f"{PROMPT}\nStudent: {student_question}\nProfessor: {professor_response}")
    return response.text.strip().lower() == "yes"
