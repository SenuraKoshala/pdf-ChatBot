from src.agent_planner import plan_tools
from src.tool_executor import execute_tool
from src.chatbot import model

def run_multi_agent(question):

    # STEP 1: PLAN
    plan = plan_tools(question)

    print("\n[PLAN]")
    print(plan)

    tool_results = []

    # STEP 2: EXECUTE EACH TOOL
    for step in plan:

        tool = step["tool"]
        tool_input = step["input"]

        print(f"\n[EXECUTING] {tool}: {tool_input}")

        result = execute_tool(tool, tool_input)

        tool_results.append({
            "tool": tool,
            "input": tool_input,
            "result": result
        })

    # STEP 3: BUILD CONTEXT
    context = ""

    for item in tool_results:

        context += f"""
Tool: {item['tool']}
Input: {item['input']}
Result: {item['result']}
"""
    
    # STEP 4: FINAL ANSWER
    final_prompt = f"""
You are a helpful AI assistant.

Use the tool results below to answer.

{context}

User Question:
{question}

Final Answer:
"""

    response = model.generate_content(final_prompt)

    return response.text