# Resume RAG Chatbot

## Overview

A production-style Resume RAG (Retrieval-Augmented Generation) application built using:

* Streamlit (Frontend)
* FastAPI (Backend)
* LangChain
* OpenAI
* FAISS Vector Database
* Docker

The application allows users to upload TXT or PDF resumes and ask questions about skills, projects, experience, and education.

---

## Architecture

User

↓

Streamlit Frontend

↓

FastAPI Backend

↓

FAISS Vector Database

↓

OpenAI GPT

↓

Answer

---

## Features

* Multi-document upload
* PDF and TXT support
* Semantic Search
* Embeddings
* FAISS Vector Database
* FastAPI REST APIs
* Streamlit Chat Interface
* Docker Support
* Retrieval-Augmented Generation (RAG)

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### AI Stack

* LangChain
* OpenAI
* FAISS

### Deployment

* Docker

---

## Run Backend

```bash
uvicorn backend:app --reload
```

Backend URL:

```text
http://localhost:8000/docs
```

---

## Run Frontend

```bash
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## Docker

Build Image:

```bash
docker build -t resume-rag-api .
```

Run Container:

```bash
docker run -p 8000:8000 --env-file .env resume-rag-api
```

---

## Author

Nithish C

Generative AI Engineer
