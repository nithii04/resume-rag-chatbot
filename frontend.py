# 01
import streamlit as st
# 02
import requests
# 03
from pypdf import PdfReader

# 04
BACKEND_URL = "http://127.0.0.1:8000"

# 05
st.set_page_config(
    page_title="Resume Chat Bot",
    page_icon="📄",
    layout="centered"
)

# 06
st.title("📄 Resume RAG Chatbot")
# 07
st.write("Ask questions about the candidate's skills, projects, experience, and education.")

# 08
st.sidebar.markdown("""
# About Project

This project uses **RAG (Retrieval-Augmented Generation)** to answer questions from resume documents.

### Sample Questions

1. What are my skills?
2. What projects have I completed?
3. What is my work experience?
4. What technologies do I know?
""")

# 09
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 10
if "document_uploaded" not in st.session_state:
    st.session_state["document_uploaded"] = False

# 11
if "uploaded_file_names" not in st.session_state:
    st.session_state["uploaded_file_names"] = []

# 12
if st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = []
    st.session_state["document_uploaded"] = False
    st.session_state["uploaded_file_names"] = []
    st.rerun()

# 13
uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

# 14
if uploaded_files:
    current_file_names = [file.name for file in uploaded_files]

    # Upload only when new files are selected
    if current_file_names != st.session_state["uploaded_file_names"]:
        all_text = ""

        # 15
        for uploaded_file in uploaded_files:
            all_text += f"\n\n===== FILE: {uploaded_file.name} =====\n\n"

            # 16
            if uploaded_file.name.endswith(".txt"):
                all_text += uploaded_file.read().decode("utf-8")

            # 17
            elif uploaded_file.name.endswith(".pdf"):
                pdf_reader = PdfReader(uploaded_file)

                # 18
                for page_num, page in enumerate(pdf_reader.pages, start=1):
                    extracted_text = page.extract_text()

                    # 19
                    if extracted_text:
                        all_text += f"\n--- Page {page_num} ---\n"
                        all_text += extracted_text

        # 20
        if not all_text.strip():
            st.error("No text could be extracted from the uploaded files.")
        else:
            with st.spinner("Uploading documents to backend..."):
                # 21
                requests.post(f"{BACKEND_URL}/reset")

                # 22
                upload_response = requests.post(
                    f"{BACKEND_URL}/upload",
                    params={"text": all_text}
                )

            # 23
            if upload_response.status_code == 200:
                st.session_state["document_uploaded"] = True
                st.session_state["uploaded_file_names"] = current_file_names
                st.session_state["messages"] = []
                st.success("Documents uploaded successfully.")
            else:
                st.error("Failed to upload documents to backend.")

# 24
if uploaded_files and st.session_state["document_uploaded"]:

    # 25
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

            # 26
            if message["role"] == "assistant" and "sources" in message:
                with st.expander("📌 Sources Used"):
                    for source in message["sources"]:
                        st.markdown(f"**Source {source['source_id']}**")
                        st.write(source["content"])

    # 27
    query = st.text_input("Ask a question:")

    # 28
    if st.button("Ask"):
        if query:
            # 29
            st.session_state["messages"].append(
                {
                    "role": "user",
                    "content": query
                }
            )

            # 30
            with st.spinner("Getting answer from FastAPI backend..."):
                api_response = requests.post(
                    f"{BACKEND_URL}/ask",
                    params={"question": query}
                )

            # 31
            if api_response.status_code == 200:
                result = api_response.json()
                answer = result.get("answer", "No answer returned.")
                sources = result.get("sources", [])

                # 32
                st.session_state["messages"].append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    }
                )

                # 33
                st.rerun()
            else:
                st.error("Backend failed to return an answer.")

        else:
            # 34
            st.warning("Please enter a question.")

# 35
else:
    st.info("Please upload TXT or PDF file to start.")