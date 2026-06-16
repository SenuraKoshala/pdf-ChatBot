from src.tools.pdf_search import search_pdf
from src.tools.calculator import calculator

def choose_tool(question):

    question = question.lower()

    if any(
        word in question
        for word in [
            "calculate",
            "+",
            "-",
            "*",
            "/"
        ]
    ):
        return "calculator"

    return "pdf_search"


def run_agent(question):

    tool = choose_tool(
        question
    )

    if tool == "calculator":

        expression = (
            question
            .replace("calculate", "")
            .strip()
        )

        result = calculator(
            expression
        )

        return {
            "tool": tool,
            "result": result
        }

    elif tool == "pdf_search":

        result = search_pdf(
            question
        )

        return {
            "tool": tool,
            "result": result
        }