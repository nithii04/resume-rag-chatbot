from fastapi import FastAPI
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

load_dotenv()

app = FastAPI()

vector_db = None

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


@app.get("/")
def home():
    return {"message": "Resume RAG API Running"}


@app.post("/upload")
def upload_document(text: str):
    global vector_db

    documents = [Document(page_content=text)]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(docs, embeddings)

    return {"message": "Document uploaded successfully"}


@app.post("/ask")
def ask_question(question: str):
    global vector_db

    if vector_db is None:
        return {
            "question": question,
            "answer": "Please upload a document first."
        }

    search_query = question + " projects professional experience work experience responsibilities"

    retrieved_docs = vector_db.similarity_search(search_query, k=5)

    context = "\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a resume assistant.

Answer the question using only the resume context.
If the answer is not available in the resume, say:
"I could not find this information in the uploaded document."

Resume Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "question": question,
        "answer": response.content
    }