from pydantic import BaseModel
from datetime import datetime

class PDFMetadataBase(BaseModel):
    filename: str
    upload_date: datetime

class PDFMetadataCreate(PDFMetadataBase):
    text_content: str

class PDFMetadata(PDFMetadataBase):
    id: int

    class Config:
        orm_mode = True

class Question(BaseModel):
    pdf_id: int
    question: str

class Answer(BaseModel):
    answer: str
