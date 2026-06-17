# Resume RAG Chatbot Notes

## Project Overview

Resume RAG Chatbot built using:

* Streamlit
* FastAPI
* LangChain
* OpenAI
* FAISS
* Docker

---

## Architecture

User

↓

Streamlit Frontend

↓

FastAPI Backend

↓

Embeddings

↓

FAISS Vector DB

↓

Similarity Search

↓

OpenAI GPT

↓

Answer

---

## Important Concepts

### What is RAG?

Retrieval-Augmented Generation is a technique where relevant information is retrieved from documents and provided to an LLM before generating an answer.

### Why Chunking?

Large documents are split into smaller chunks so embeddings can be generated efficiently and relevant information can be retrieved.

### Why Embeddings?

Embeddings convert text into numerical vectors that capture semantic meaning.

### Why FAISS?

FAISS stores embeddings and performs fast similarity search.

### What does similarity_search() do?

Finds the most relevant chunks for a user query.

### Why FastAPI?

FastAPI exposes the RAG system through APIs.

### Why Streamlit?

Streamlit provides a simple user interface.

---

## APIs

### Upload Document

POST /upload

Purpose:

* Receive document text
* Create chunks
* Create embeddings
* Create vector database

### Ask Question

POST /ask

Purpose:

* Search relevant chunks
* Build prompt
* Query LLM
* Return answer

---

## Commands

Run Backend:

uvicorn backend:app --reload

Run Frontend:

streamlit run frontend.py --server.port 8506

Docker Build:

docker build -t resume-rag-api .

Docker Run:

docker run -p 8000:8000 --env-file .env resume-rag-api

---

## Lessons Learned

* Frontend = UI
* Backend = Business Logic
* API = Communication Layer
* Embeddings = Text to Vector
* FAISS = Vector Database
* RAG = Retrieval + Generation
* Docker = Package Application
* GitHub = Version Control
