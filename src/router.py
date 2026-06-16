from src.chatbot import model

def choose_tool(question):

    prompt = f"""
You are a routing agent.

Available tools:

1. calculator
   Use for mathematical calculations.

2. pdf_search
   Use for answering questions from PDFs.

User Question:
{question}

Return ONLY ONE WORD:

calculator
or
pdf_search
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()