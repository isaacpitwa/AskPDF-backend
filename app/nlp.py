from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings,Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import PDFMetadata
from typing import List
import logging
import sys
import os


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Configuration for embedding model and LLM
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm= Ollama(model="llama3", request_timeout=360.0)



def get_pdf_texts_from_db(db: Session) -> List[str]:
    pdfs = db.query(PDFMetadata).all()
    return [pdf.text_content for pdf in pdfs]

def create_documents_from_texts(text: str) -> Document:
    document = Document(text=text)
    return document

def index_documents(document: Document):
    index = VectorStoreIndex.from_documents([document])
    return index

def get_answer_from_index(index, question: str) -> str:
    try: 
        query_engine = index.as_query_engine()
        response = query_engine.query(question)
        return response
    except Exception as e:
        print(f"Failed to use local HuggingFace model: {e}")
        return "An error occurred while querying the local HuggingFace model."

def get_answer_from_pdf(question: str, text_content:str) -> str:
    # Create a database session
    db = SessionLocal()
    try:
        
        # Create documents from texts
        documents = create_documents_from_texts(text_content)
        
        # Index the documents
        index = index_documents(documents)
        
        # Get the answer from the index
        prediction = get_answer_from_index(index, question)
        answer = str(prediction)
    finally:
        db.close()
    
    return answer
