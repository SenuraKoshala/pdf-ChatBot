from google.genai import types
from src.chatbot import client
from src.tool_executor import execute_tool

MODEL = "gemini-2.5-flash"

TOOLS = [
    types.Tool(function_declarations=[
        types.FunctionDeclaration(
            name="pdf_search",
            description="Search PDF documents for information about a topic",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "question": types.Schema(
                        type=types.Type.STRING,
                        description="The question to search for in the PDFs"
                    )
                },
                required=["question"]
            )
        ),
        types.FunctionDeclaration(
            name="calculator",
            description="Evaluate a math expression and return the numeric result",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "expression": types.Schema(
                        type=types.Type.STRING,
                        description="The math expression to evaluate, e.g. 15 * 20"
                    )
                },
                required=["expression"]
            )
        )
    ])
]

def run_multi_agent(question):

    contents = [types.Content(role="user", parts=[types.Part(text=question)])]

    while True:

        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=types.GenerateContentConfig(tools=TOOLS)
        )

        candidate = response.candidates[0]
        contents.append(candidate.content)

        function_calls = [p for p in candidate.content.parts if p.function_call]

        if not function_calls:
            return response.text

        tool_response_parts = []

        for part in function_calls:
            fc = part.function_call
            args = dict(fc.args)
            print(f"\n[TOOL CALL] {fc.name}({args})")

            if fc.name == "pdf_search":
                result = execute_tool("pdf_search", args["question"])
            elif fc.name == "calculator":
                result = execute_tool("calculator", args["expression"])
            else:
                result = "Unknown tool"

            print(f"[RESULT] {result}")

            tool_response_parts.append(
                types.Part(
                    function_response=types.FunctionResponse(
                        name=fc.name,
                        response={"result": result}
                    )
                )
            )

        contents.append(types.Content(role="user", parts=tool_response_parts))
