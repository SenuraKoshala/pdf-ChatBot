import chromadb
from pprint import pprint

client = chromadb.PersistentClient(path="db")

collection = client.get_collection(
    name="pdf_collection"
)

data = collection.get()

pprint(data)