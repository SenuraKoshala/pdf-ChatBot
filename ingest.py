from src.pdf_reader import read_all_pdfs
from src.chunker import chunk_text
from src.vector_store import add_chunks

from src.config import PDF_FOLDER

documents = read_all_pdfs(PDF_FOLDER)

all_chunks = []

for document in documents:

    chunks = chunk_text(
        document["text"]
    )

    for chunk in chunks:

        all_chunks.append(
            {
                "text": chunk,
                "source": document["filename"]
            }
        )

print(
    f"Total chunks: {len(all_chunks)}"
)

add_chunks(all_chunks)

print("Done.")