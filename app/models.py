from sqlalchemy import Column, Integer, String, DateTime, Text
from .database import Base
from datetime import datetime  # Add this line


class PDFMetadata(Base):
    __tablename__ = "pdf_metadata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    upload_date = Column(DateTime)
    text_content = Column(Text)


class QuestionHistory(Base):
    __tablename__ = "question_history"

    id = Column(Integer, primary_key=True, index=True)
    pdf_id = Column(Integer, index=True)
    question = Column(Text)
    answer = Column(Text)
    asked_at = Column(DateTime, default=datetime.utcnow)  # Fix the line
