from src.embedder import get_embedding
from src.vector_store import search
from src.chatbot import ask_llm

print("PDF Chatbot Ready")

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    # Create embedding for question
    query_embedding = get_embedding(question)

    # Search vector database
    results = search(query_embedding)

    # Get matching chunks
    documents = results["documents"][0]

    # Get metadata
    metadatas = results["metadatas"][0]

    # Build context
    context = "\n\n".join(documents)

    # Extract source names
    sources = []

    for metadata in metadatas:
        sources.append(metadata["source"])

    # Ask Gemini
    answer = ask_llm(
        context,
        question
    )

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for source in set(sources):
        print(f"- {source}")