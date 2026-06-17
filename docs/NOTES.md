# Resume RAG Chatbot - Learning Notes

## Project Goal

Build a production-style Resume RAG Chatbot capable of answering questions from uploaded PDF and TXT documents.

---

## Concepts Learned

### RAG (Retrieval Augmented Generation)

RAG combines:

* Retrieval
* Large Language Models

Flow:

User Question
↓
Retrieve Relevant Chunks
↓
Provide Context
↓
Generate Answer

---

### Chunking

Used:

* RecursiveCharacterTextSplitter

Purpose:

* Split large documents into smaller chunks
* Improve retrieval quality

---

### Embeddings

Used:

* OpenAI Embeddings

Purpose:

* Convert text into vectors
* Enable semantic search

---

### Vector Database

Used:

* FAISS

Purpose:

* Store embeddings
* Perform similarity search

---

### Hybrid Search

Implemented:

* FAISS Search
* BM25 Search

Purpose:

* Combine semantic search and keyword search

Benefits:

* Better retrieval accuracy
* Improved document understanding

---

### Cross Encoder Reranking

Used:

* cross-encoder/ms-marco-MiniLM-L-6-v2

Purpose:

* Rank retrieved chunks
* Select most relevant context

---

### FastAPI

Purpose:

* Backend API
* Document upload
* Question answering

Endpoints:

* /upload
* /ask
* /reset

---

### Streamlit

Purpose:

* Frontend UI
* File Upload
* Chat Interface
* Source Display

---

### Docker

Purpose:

* Containerize application
* Easy deployment

Commands:

docker build -t resume-rag-api .

docker run -p 8000:8000 resume-rag-api

---

## Challenges Faced

### Challenge 1

Problem:

Old documents remained in Vector DB.

Solution:

Created /reset endpoint.

---

### Challenge 2

Problem:

Poor retrieval quality.

Solution:

Implemented Hybrid Search.

---

### Challenge 3

Problem:

Important chunks were not selected.

Solution:

Added Cross Encoder Reranking.

---

## Future Improvements

* Multi Query Retrieval
* Conversational Memory
* RAGAS Evaluation
* Resume Comparison
* ATS Scoring
* Resume Improvement Suggestions

---

## Key Learning

Retrieval quality is more important than changing the LLM.

Better Retrieval
↓
Better Context
↓
Better Answers
