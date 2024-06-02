import os
import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import fitz  # PyMuPDF

from .database import SessionLocal, engine
from . import models, schemas, crud
from .nlp import get_answer_from_pdf

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIRECTORY = "./uploaded_pdfs/"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload_pdf/", response_model=schemas.PDFMetadata)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    pdf_document = fitz.open(file_path)
    text_content = ""
    for page_num in range(pdf_document.page_count):
        text_content += pdf_document.load_page(page_num).get_text()

    pdf_metadata = schemas.PDFMetadataCreate(
        filename=file.filename,
        upload_date=datetime.datetime.now(),
        text_content=text_content
    )
    
    db_pdf = crud.create_pdf_metadata(db=db, pdf_metadata=pdf_metadata)
    return db_pdf

@app.post("/ask_question/", response_model=schemas.Answer)
async def ask_question(question: schemas.Question, db: Session = Depends(get_db)):
    pdf_metadata = crud.get_pdf_metadata(db, question.pdf_id)
    if not pdf_metadata:
        raise HTTPException(status_code=404, detail="PDF not found")

    answer = get_answer_from_pdf(question.question,pdf_metadata.text_content)
    return {"answer": answer}
