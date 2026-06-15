from src.embedder import get_embedding
from src.vector_store import search
from src.chatbot import ask_llm

print("PDF Chatbot Ready")

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    query_embedding = get_embedding(
        question
    )

    results = search(
        query_embedding
    )

    context = "\n".join(
        results["documents"][0]
    )

    answer = ask_llm(
        context,
        question
    )

    print("\nAnswer:")
    print(answer)