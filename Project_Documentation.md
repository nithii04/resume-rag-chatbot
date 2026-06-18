# Resume RAG Chatbot

## Project Overview

Resume RAG Chatbot is an AI-powered application that allows users to upload one or more resumes (PDF/TXT) and ask natural language questions about the candidate.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the uploaded documents and generate accurate responses using a Large Language Model (LLM).

The project follows a production-style architecture by separating:

* Frontend (Streamlit)
* Backend API (FastAPI)
* Vector Database (FAISS)
* Embedding Model (OpenAI Embeddings)
* Language Model (GPT-4o-mini)

---

# Problem Statement

Recruiters and hiring managers often spend significant time manually reviewing resumes to extract information such as:

* Skills
* Projects
* Work Experience
* Education
* Certifications
* Technologies Used

This project automates the process by enabling conversational search over resumes.

---

# Objectives

* Upload resume documents.
* Extract text from PDF/TXT files.
* Convert documents into searchable chunks.
* Store embeddings in a vector database.
* Retrieve relevant information for user queries.
* Generate context-aware answers.
* Display source chunks used for answering.

---

# Technology Stack

## Frontend

* Streamlit

## Backend

* FastAPI

## LLM

* GPT-4o-mini

## Embeddings

* OpenAI Embeddings

## Vector Database

* FAISS

## PDF Processing

* PyPDF

## Language

* Python

---

# System Architecture

User Uploads Resume

↓

Frontend (Streamlit)

↓

Backend API (FastAPI)

↓

Document Chunking

↓

OpenAI Embeddings

↓

FAISS Vector Database

↓

User Question

↓

Retriever

↓

Relevant Chunks

↓

GPT-4o-mini

↓

Final Answer

---

# Project Workflow

## Step 1: Upload Resume

User uploads:

* PDF
* TXT

through Streamlit UI.

---

## Step 2: Text Extraction

PDF documents are processed using:

PyPDF

Extracted text is combined into a single document.

---

## Step 3: Document Chunking

Large documents are split using:

RecursiveCharacterTextSplitter

Configuration:

* Chunk Size = 1000
* Chunk Overlap = 200

Benefits:

* Better retrieval
* Preserves context
* Improves accuracy

---

## Step 4: Embedding Generation

Each chunk is converted into vector embeddings using:

OpenAIEmbeddings

Purpose:

* Transform text into numerical vectors
* Enable semantic search

---

## Step 5: Vector Database Creation

Embeddings are stored in:

FAISS

Benefits:

* Fast similarity search
* Lightweight
* Efficient retrieval

---

## Step 6: User Query

Example Questions:

* What are Nithish's skills?
* What projects has he worked on?
* Which cloud platforms does he know?
* Summarize the resume.

---

## Step 7: Retrieval

The retriever performs:

MMR Search

Configuration:

* k = 10
* fetch_k = 30

Benefits:

* Retrieves diverse chunks
* Avoids duplicate context
* Improves answer quality

---

## Step 8: Context Building

Retrieved chunks are merged:

Chunk 1

Chunk 2

Chunk 3

...

Chunk N

↓

Context

---

## Step 9: LLM Processing

Prompt contains:

* User Question
* Retrieved Context
* Instructions

GPT-4o-mini generates the final answer.

---

## Step 10: Source Citation

Retrieved chunks are returned alongside the answer.

Frontend displays:

📌 Sources Used

Benefits:

* Transparency
* Explainability
* Easier debugging

---

# API Endpoints

## GET /

Health Check Endpoint

Response:

{
"message": "Resume RAG API Running"
}

---

## POST /upload

Uploads extracted document text.

Input:

text

Output:

{
"message": "Document uploaded successfully"
}

---

## POST /ask

Input:

question

Output:

{
"question": "...",
"answer": "...",
"sources": [...]
}

---

## POST /reset

Clears Vector Database.

Output:

{
"message": "Vector DB reset successfully"
}

---

# Features Implemented

### Multiple Document Upload

Supports:

* PDF
* TXT

---

### Chat History

Stores previous conversations.

---

### Source Citations

Displays chunks used for answering.

---

### Clear Chat

Clears conversation only.

---

### Reset Document

Clears:

* Vector Database
* Uploaded Documents
* Chat History

---

### MMR Retrieval

Improves retrieval quality.

---

### Resume Summarization

Generates professional profile summaries.

---

# Challenges Faced

## Challenge 1

Answers returning:

"I could not find this information."

Solution:

* Increased chunk size
* Improved prompt engineering
* Enhanced retrieval

---

## Challenge 2

Wrong chunks being retrieved.

Solution:

* Switched to MMR Retrieval
* Increased fetch_k

---

## Challenge 3

Ask button disappearing after Clear Chat.

Solution:

* Managed session state properly
* Separated Clear Chat and Reset Document

---

## Challenge 4

Missing source transparency.

Solution:

* Added source citation panel

---

# Future Enhancements

## Hybrid Search

Combine:

* Vector Search
* BM25 Keyword Search

Benefits:

* Better retrieval
* Improved accuracy

---

## Reranking

Use:

* Cross Encoder
* Cohere Rerank

Benefits:

* More relevant context

---

## Multi Resume Comparison

Compare:

* Candidate A
* Candidate B

---

## Resume Scoring

Match resumes against job descriptions.

---

## Agentic AI

Allow chatbot to:

* Search
* Analyze
* Compare
* Recommend

---

## Cloud Deployment

Deploy on:

* AWS
* Azure
* GCP

---

# Learning Outcomes

Through this project I learned:

* RAG Architecture
* Prompt Engineering
* Vector Databases
* Embeddings
* FastAPI
* Streamlit
* OpenAI APIs
* Retrieval Optimization
* Source Citation
* Production Style Architecture

---

# Conclusion

Resume RAG Chatbot demonstrates an end-to-end implementation of Retrieval-Augmented Generation using FastAPI, Streamlit, FAISS, OpenAI Embeddings, and GPT-4o-mini. The project enables intelligent question-answering over resumes and provides a strong foundation for building production-grade GenAI applications.
