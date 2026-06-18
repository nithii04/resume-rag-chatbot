# 🚀 Resume RAG Chatbot

A production-style Resume RAG (Retrieval-Augmented Generation) Chatbot built using Streamlit, FastAPI, OpenAI, LangChain, FAISS, BM25 Hybrid Search, and Cross-Encoder Reranking.

The application allows users to upload PDF/TXT resumes and ask natural language questions about the document. The system retrieves relevant content using Hybrid Search and generates accurate answers using LLMs.

---

# 📌 Features

### Document Processing

* Upload PDF documents
* Upload TXT documents
* Multi-document support
* Automatic text extraction
* Chunking and preprocessing

### Retrieval Pipeline

* OpenAI Embeddings
* FAISS Vector Database
* BM25 Keyword Search
* Hybrid Search (FAISS + BM25)
* Cross-Encoder Re-ranking
* Source Citation Support

### LLM Features

* Question Answering
* Resume Analysis
* Skills Extraction
* Experience Summarization
* Project Identification
* Technology Extraction
* Cloud Skills Identification

### User Interface

* Streamlit Frontend
* Chat Interface
* Source Display
* Clear Chat Option
* Upload Status Tracking

### Backend

* FastAPI REST API
* Modular Architecture
* API Documentation
* Docker Support

---

# 🏗️ System Architecture

User
↓
Streamlit Frontend
↓
FastAPI Backend
↓
Query Expansion
↓
Hybrid Retrieval

FAISS Vector Search
+
BM25 Keyword Search

↓
Cross Encoder Re-ranking
↓
Top Relevant Chunks
↓
GPT-4o-mini
↓
Answer Generation
↓
Source Citations

---

# 🧠 RAG Pipeline

### Step 1: Document Upload

User uploads:

* PDF Resume
* TXT Resume

### Step 2: Text Extraction

PDF files are processed using:

* pypdf

### Step 3: Chunking

Documents are split using:

* RecursiveCharacterTextSplitter

### Step 4: Embeddings

OpenAI Embeddings convert chunks into vectors.

### Step 5: Vector Storage

Vectors are stored inside:

* FAISS

### Step 6: Hybrid Retrieval

Retrieval combines:

* Semantic Search (FAISS)
* Keyword Search (BM25)

### Step 7: Cross Encoder Re-ranking

Retrieved chunks are ranked using:

* cross-encoder/ms-marco-MiniLM-L-6-v2

### Step 8: Answer Generation

Top-ranked chunks are sent to:

* GPT-4o-mini

### Step 9: Source Citations

Relevant chunks are displayed as sources.

---

# ⚙️ Tech Stack

## Frontend

* Streamlit

## Backend

* FastAPI

## LLM

* OpenAI GPT-4o-mini

## RAG Framework

* LangChain

## Embeddings

* OpenAI Embeddings

## Vector Database

* FAISS

## Retrieval

* BM25
* Hybrid Search

## Re-ranking

* Sentence Transformers
* Cross Encoder

## Containerization

* Docker

---

# 📂 Project Structure

resume-rag-chatbot/

├── frontend.py

├── backend.py

├── requirements.txt

├── Dockerfile

├── README.md

├── .gitignore

├── .dockerignore

├── data/

├── docs/

│ └── NOTES.md

└── archive/

---

# 🚀 Installation

## Clone Repository

git clone https://github.com/your-github-username/resume-rag-chatbot.git

cd resume-rag-chatbot

---

## Create Virtual Environment

python -m venv .venv

### Activate

Windows:

.venv\Scripts\activate

Linux/Mac:

source .venv/bin/activate

---

## Install Dependencies

pip install -r requirements.txt

---

# 🔐 Environment Variables

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here

---

# ▶️ Run Backend

uvicorn backend:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

---

# ▶️ Run Frontend

streamlit run frontend.py

Frontend URL:

http://localhost:8501

---

# 🐳 Docker

## Build Image

docker build -t resume-rag-api .

## Run Container

docker run -p 8000:8000 --env-file .env resume-rag-api

---

# 📊 Example Questions

* What are the candidate's technical skills?
* What projects has the candidate worked on?
* Summarize professional experience.
* What cloud technologies does the candidate know?
* Which machine learning algorithms are mentioned?
* Create a professional LinkedIn summary.

---

# 🔥 Advanced RAG Techniques Used

✅ OpenAI Embeddings

✅ FAISS Vector Database

✅ BM25 Keyword Search

✅ Hybrid Search

✅ Cross Encoder Re-ranking

✅ Source Citations

✅ FastAPI Backend

✅ Streamlit Frontend

✅ Docker Containerization

---

# 🎯 Future Improvements

* Multi Query Retrieval
* Conversational Memory
* RAGAS Evaluation
* Multi Resume Comparison
* Resume Scoring System
* ATS Compatibility Analysis
* Resume Improvement Suggestions
* Multi-LLM Support
* Authentication & User Management

---

# 👨‍💻 Author

Nithish C

Generative AI Engineer

Skills:

* Python
* LangChain
* RAG
* FastAPI
* Streamlit
* OpenAI
* AWS
* Docker
* Generative AI
