from src.embedder import get_embedding
from src.vector_store import search

def search_pdf(question):

    query_embedding = get_embedding(
        question
    )

    results = search(
        query_embedding
    )

    documents = results["documents"][0]

    context = "\n".join(documents)

    return context