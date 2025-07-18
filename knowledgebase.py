from agno.embedder.google import GeminiEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb
import os

from dotenv import load_dotenv

load_dotenv()

vector_db = LanceDb(
    table_name="recipes",
    uri="/tmp/lancedb",  
    embedder=GeminiEmbedder(api_key=os.getenv('GOOGLE_API_KEY')),
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)
knowledge_base.load(recreate=False)  

