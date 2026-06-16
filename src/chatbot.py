import google.generativeai as genai

from src.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ask_llm(context, question):

    prompt = f"""
You are a helpful assistant.

Use ONLY the provided context to answer.

If the answer is not found in the context,
say:

"I could not find that information in the documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(
        prompt
    )

    return response.text