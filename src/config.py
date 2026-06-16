from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PDF_FOLDER = "data"

CHROMA_PATH = "db"

COLLECTION_NAME = "pdf_collection"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"