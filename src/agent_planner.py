from src.chatbot import model
import json

def plan_tools(question):

    prompt = f"""
You are an AI planner.

You can use these tools:

1. pdf_search
- Use for questions about documents

2. calculator
- Use for math expressions

Return a JSON list of steps.

Format:
[
  {{
    "tool": "tool_name",
    "input": "input for tool"
  }}
]

Rules:
- Use multiple tools if needed
- Keep input clean
- Return ONLY valid JSON

User Question:
{question}
"""

    response = model.generate_content(prompt)

    print("\nRAW MODEL OUTPUT:\n")
    print(response.text)

    raw = response.text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()
    return json.loads(raw)
