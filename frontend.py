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

if "uploaded_file_names" not in st.session_state:
    st.session_state["uploaded_file_names"] = []

if "uploader_key" not in st.session_state:
    st.session_state["uploader_key"] = 0

if st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = []
    st.rerun()

if st.sidebar.button("Reset Document"):
    requests.post(f"{BACKEND_URL}/reset")
    st.session_state["messages"] = []
    st.session_state["document_uploaded"] = False
    st.session_state["uploaded_file_names"] = []
    st.session_state["uploader_key"] += 1
    st.rerun()

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["txt", "pdf"],
    accept_multiple_files=True,
    key=f"file_uploader_{st.session_state['uploader_key']}"
)

if uploaded_files:
    current_file_names = [file.name for file in uploaded_files]

    if current_file_names != st.session_state["uploaded_file_names"]:
        all_text = ""

        for uploaded_file in uploaded_files:
            all_text += f"\n\n===== FILE: {uploaded_file.name} =====\n\n"

            if uploaded_file.name.endswith(".txt"):
                all_text += uploaded_file.read().decode("utf-8")

            elif uploaded_file.name.endswith(".pdf"):
                pdf_reader = PdfReader(uploaded_file)

                for page_num, page in enumerate(pdf_reader.pages, start=1):
                    extracted_text = page.extract_text()

                    if extracted_text:
                        all_text += f"\n--- Page {page_num} ---\n"
                        all_text += extracted_text

        if not all_text.strip():
            st.error("No text could be extracted from the uploaded files.")
        else:
            with st.spinner("Uploading documents to backend..."):
                requests.post(f"{BACKEND_URL}/reset")

                upload_response = requests.post(
                    f"{BACKEND_URL}/upload",
                    params={"text": all_text}
                )

            if upload_response.status_code == 200:
                st.session_state["document_uploaded"] = True
                st.session_state["uploaded_file_names"] = current_file_names
                st.session_state["messages"] = []
                st.success("Documents uploaded successfully.")
            else:
                st.error("Failed to upload documents to backend.")

if st.session_state["document_uploaded"]:
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

            if message["role"] == "assistant" and "sources" in message:
                with st.expander("📌 Sources Used"):
                    for source in message["sources"]:
                        st.markdown(f"**Source {source['source_id']}**")
                        st.write(source["content"])

    query = st.text_input("Ask a question:")

    if st.button("Ask"):
        if query:
            st.session_state["messages"].append(
                {
                    "role": "user",
                    "content": query
                }
            )

            with st.spinner("Getting answer from FastAPI backend..."):
                api_response = requests.post(
                    f"{BACKEND_URL}/ask",
                    params={"question": query}
                )

            if api_response.status_code == 200:
                result = api_response.json()
                answer = result.get("answer", "No answer returned.")
                sources = result.get("sources", [])

                st.session_state["messages"].append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    }
                )

                st.rerun()
            else:
                st.error("Backend failed to return an answer.")

        else:
            st.warning("Please enter a question.")
else:
    st.info("Please upload TXT or PDF file to start.")