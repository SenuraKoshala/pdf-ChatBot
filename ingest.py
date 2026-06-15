from src.pdf_reader import read_pdf
from src.chunker import chunk_text
from src.vector_store import add_chunks

from src.config import PDF_PATH

print("Reading PDF...")

text = read_pdf(PDF_PATH)

print("Chunking...")

chunks = chunk_text(text)

print(f"Chunks: {len(chunks)}")

add_chunks(chunks)

print("Stored in Vector DB.")