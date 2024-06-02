from sqlalchemy.orm import Session
from . import models, schemas

def get_pdf_metadata(db: Session, pdf_id: int):
    return db.query(models.PDFMetadata).filter(models.PDFMetadata.id == pdf_id).first()

def create_pdf_metadata(db: Session, pdf_metadata: schemas.PDFMetadataCreate):
    db_pdf_metadata = models.PDFMetadata(**pdf_metadata.dict())
    db.add(db_pdf_metadata)
    db.commit()
    db.refresh(db_pdf_metadata)
    return db_pdf_metadata

def log_question(db: Session, question: schemas.Question, answer: str):
    db_question = models.QuestionHistory(
        pdf_id=question.pdf_id,
        question=question.question,
        answer=answer
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
