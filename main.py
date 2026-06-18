from src.multi_agent import run_multi_agent

print("Multi-tool Agent Ready")

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = run_multi_agent(question)

    print("\nANSWER:\n", answer)