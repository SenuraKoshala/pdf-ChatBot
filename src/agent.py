from src.tools.pdf_search import search_pdf
from src.tools.calculator import calculator
from src.router import choose_tool
from src.chatbot import model


def run_agent(question):

    tool = choose_tool(question)

    print(f"\n[Tool Selected] {tool}")

    if tool == "calculator":

        expression_prompt = f"""
Extract ONLY the mathematical expression.

Question:
{question}

Return only the expression.
"""

        expression = (
            model.generate_content(
                expression_prompt
            )
            .text
            .strip()
        )

        print(f"\n[Expression Extracted] {expression}")

        result = calculator(
            expression
        )
        print(f"\n[Calculation Result] {result}")

        return {
            "tool": tool,
            "result": result
        }

    elif tool == "pdf_search":

        result = search_pdf(
            question
        )
        print(f"\n[PDF Search Result] {result[:200]}...")

        return {
            "tool": tool,
            "result": result
        }