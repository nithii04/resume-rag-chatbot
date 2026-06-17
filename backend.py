from fastapi import FastAPI
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder

vector_db = None
all_docs = []
bm25 = None
tokenized_docs = []

load_dotenv()

app = FastAPI()

vector_db = None

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


@app.get("/")
def home():
    return {"message": "Resume RAG API Running"}


@app.post("/reset")
def reset_vector_db():
    global vector_db
    vector_db = None
    return {"message": "Vector DB reset successfully"}


@app.post("/upload")
def upload_document(text: str):
    global vector_db

    documents = [
        Document(page_content=text)
    ]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    docs = splitter.split_documents(documents)
    global all_docs, bm25, tokenized_docs

    all_docs = docs

    tokenized_docs = [
        doc.page_content.lower().split()
        for doc in docs
]

    bm25 = BM25Okapi(tokenized_docs)
    print(f"Total Chunks Created: {len(docs)}")

    for i, doc in enumerate(docs):
        print(f"\nCHUNK {i+1}")
        print(doc.page_content[:500])

    embeddings = OpenAIEmbeddings()

    vector_db = FAISS.from_documents(docs, embeddings)

    return {
        "message": "Document uploaded successfully",
        "chunks_created": len(docs)
    }

def build_search_query(question: str) -> str:
    q = question.lower()

    if "programming" in q or "language" in q:
        return f"""
{question}
programming languages
programming scripting languages
python c c++ perl java sql
development tools
technical skills
libraries frameworks
"""

    if "skill" in q or "technology" in q or "tools" in q:
        return f"""
{question}
technical skills
core competency
programming languages
libraries frameworks
cloud platforms
databases
devops tools
generative ai llm technologies
"""

    if "project" in q:
        return f"""
{question}
projects
professional experience
client
role
responsibilities
project description
achievements
"""

    if "experience" in q:
        return f"""
{question}
summary
total experience
professional experience
work experience
roles
companies
"""

    return f"""
{question}
summary skills projects experience education certifications technologies tools responsibilities achievements
"""

def hybrid_retrieval(query: str, top_k: int = 10):
    global vector_db, bm25, all_docs

    faiss_docs = vector_db.similarity_search(query, k=top_k)

    tokenized_query = query.lower().split()
    bm25_scores = bm25.get_scores(tokenized_query)

    top_bm25_indexes = sorted(
        range(len(bm25_scores)),
        key=lambda i: bm25_scores[i],
        reverse=True
    )[:top_k]

    bm25_docs = [all_docs[i] for i in top_bm25_indexes]

    combined_docs = []
    seen = set()

    for doc in faiss_docs + bm25_docs:
        content = doc.page_content

        if content not in seen:
            combined_docs.append(doc)
            seen.add(content)

    return combined_docs[:top_k]

def rerank_documents(question: str, docs: list, top_k: int = 5):
    pairs = []

    for doc in docs:
        pairs.append([question, doc.page_content])

    scores = reranker.predict(pairs)

    ranked_docs = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, score in ranked_docs[:top_k]]

def get_rerank_count(question):
    q = question.lower()

    if "skills" in q:
        return 12

    if "experience" in q:
        return 8

    if "project" in q:
        return 10

    return 6

@app.post("/ask")
def ask_question(question: str):
    global vector_db

    if vector_db is None:
        return {
            "question": question,
            "answer": "Please upload a document first.",
            "sources": []
        }

    search_query = f"""
{question}

skills
programming languages
technical skills
frameworks
tools
libraries
projects
experience
education
certifications
cloud
aws
azure
gcp
"""
    retrieved_docs = hybrid_retrieval(search_query, top_k=15)
    retrieved_docs = rerank_documents(question, retrieved_docs, top_k=10)
    rerank_k = get_rerank_count(question)

    retrieved_docs = rerank_documents(
        question,
        retrieved_docs,
        top_k=rerank_k
)
    print("=" * 50)
    print("QUESTION:", question)
    print("=" * 50)

    for i, doc in enumerate(retrieved_docs):
        print(f"\nSOURCE {i + 1}")
        print(doc.page_content)

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
You are an expert document assistant.

Answer using ONLY the provided context.

Rules:

1. Search all retrieved chunks carefully.
2. Combine information from multiple chunks when necessary.
3. For broad questions, organize the answer into logical categories based on the document content.
4. If information appears in different sections, merge it into a complete answer.
5. Do not invent facts.
6. If information is unavailable, say:
   "I could not find this information in the uploaded document."
7. Prefer complete answers over partial answers.

Context:
{context}

Question:
{question}

Answer:
"""    
    response = llm.invoke(prompt)

    sources = []

    for i, doc in enumerate(retrieved_docs):
        sources.append(
            {
                "source_id": i + 1,
                "content": doc.page_content
            }
        )

    return {
        "question": question,
        "answer": response.content,
        "sources": sources
    }