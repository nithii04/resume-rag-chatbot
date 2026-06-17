import streamlit as st
import requests
from pypdf import PdfReader

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Resume Chat Bot",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Resume RAG Chatbot")
st.write("Ask questions about the candidate's skills, projects, experience, and education.")

st.sidebar.markdown("""
# About Project

This project uses **RAG (Retrieval-Augmented Generation)** to answer questions from resume documents.

### Sample Questions

1. What are my skills?
2. What projects have I completed?
3. What is my work experience?
4. What technologies do I know?
""")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "document_uploaded" not in st.session_state:
    st.session_state["document_uploaded"] = False

if st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = []
    st.rerun()

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

if uploaded_files and not st.session_state["document_uploaded"]:
    all_text = ""

    for uploaded_file in uploaded_files:
        if uploaded_file.name.endswith(".txt"):
            all_text += uploaded_file.read().decode("utf-8")

        elif uploaded_file.name.endswith(".pdf"):
            pdf_reader = PdfReader(uploaded_file)

            for page in pdf_reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    all_text += extracted_text

    with st.spinner("Uploading documents to backend..."):
        upload_response = requests.post(
            f"{BACKEND_URL}/upload",
            params={"text": all_text}
        )

    if upload_response.status_code == 200:
        st.session_state["document_uploaded"] = True
        st.success("Documents uploaded successfully.")
    else:
        st.error("Failed to upload documents to backend.")

if uploaded_files:
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query = st.text_input("Ask a question:")

    if st.button("Ask"):
        if query:
            st.session_state["messages"].append(
                {"role": "user", "content": query}
            )

            with st.spinner("Getting answer from FastAPI backend..."):
                api_response = requests.post(
                    f"{BACKEND_URL}/ask",
                    params={"question": query}
                )

                answer = api_response.json()["answer"]

            st.session_state["messages"].append(
                {"role": "assistant", "content": answer}
            )

            st.rerun()

        else:
            st.warning("Please enter a question.")
else:
    st.info("Please upload TXT or PDF file to start.")