import chromadb

from src.config import (
    CHROMA_PATH,
    COLLECTION_NAME
)

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

def add_chunks(chunks):

    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[str(i)],
            documents=[chunk["text"]],
            metadatas=[
                {
                    "source": chunk["source"]
                }
            ]
        )

def search(query_embedding):

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=3
    )

    return results