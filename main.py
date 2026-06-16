from src.agent import run_agent
from src.chatbot import answer_with_context

while True:

    question = input("\nAsk: ")

    if question == "exit":
        break

    agent_result = run_agent(
        question
    )

    print(agent_result)

    answer = answer_with_context(
        agent_result["tool"],
        agent_result["result"],
        question
    )

    print("\nAnswer:")
    print(answer)