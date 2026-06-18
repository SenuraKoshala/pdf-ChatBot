from src.tools.pdf_search import search_pdf
from src.tools.calculator import calculator

def execute_tool(tool_name, tool_input):

    if tool_name == "pdf_search":
        return search_pdf(tool_input)

    elif tool_name == "calculator":
        return calculator(tool_input)

    else:
        return "Unknown tool"