
# AskPDF Application

> AskPDF is a web application that allows users to upload PDF documents, ask questions related to the content of the PDFs, and receive answers. The backend is built using FastAPI, with natural language processing (NLP) capabilities powered by LangChain and LlamaIndex. The frontend is designed using React.js, and the application uses SQLite for database management and stores uploaded PDFs in the local filesystem.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Upload PDF documents and extract text content.
- Store and manage PDF metadata and text content in a database.
- Ask questions related to the content of uploaded PDFs.
- Receive and display answers based on the PDF content.
- Follow-up questions on the same document.

## Technologies

- **Backend**: FastAPI
- **NLP Processing**: LangChain/LlamaIndex
- **Frontend**: React.js
- **Database**: SQLite
- **File Storage**: Local filesystem

## Requirements

- Python 3.8+
- pip (Python package installer)
- Ollama (Follow the installation instructions [here](https://github.com/ollama/ollama))


## Installation

### Backend

1. **Clone the repository**:
   ```bash
   git clone https://github.com/isaacpitwa/AskPDF-backend.git
   cd AskPDF-backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


### Running the Backend

1. **Start the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **API documentation**:
   - Visit `http://127.0.0.1:8000/docs` for the interactive API documentation provided by Swagger UI.

## API Endpoints

### Upload PDF

- **URL**: `/upload_pdf/`
- **Method**: `POST`
- **Description**: Uploads a PDF document and extracts its text content.
- **Request**: Multipart form data with the PDF file.
- **Response**: Metadata of the uploaded PDF.

### Ask Question

- **URL**: `/ask_question/`
- **Method**: `POST`
- **Description**: Asks a question related to the content of uploaded PDFs.
- **Request**: JSON containing the question.
- **Response**: Answer to the question.

## Project Structure

```
project-root
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── nlp.py
│
├── uploaded_pdfs
│   └── (Uploaded PDF files)
│
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides an overview of the project, setup instructions, usage guidelines, and details on the project structure. Adjust the repository URL and any specific details as needed for your project.