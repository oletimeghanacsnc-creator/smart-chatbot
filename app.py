import sys

import os

sys.path.insert(0, os.getcwd())



import streamlit as st

import PyPDF2

import io

from models.llm import get_response

from utils.rag import build_index, retrieve

from utils.search import web_search



st.set_page_config(page_title="Smart Chatbot", page_icon="🤖")

st.title("Smart Chatbot")



st.sidebar.title("Settings")

mode = st.sidebar.radio("Response Mode", ["Concise", "Detailed"])

use_search = st.sidebar.checkbox("Enable Web Search")

uploaded_file = st.sidebar.file_uploader("Upload a PDF", type="pdf")



if uploaded_file:

    try:

        pdf = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))

        text = " ".join(page.extract_text() for page in pdf.pages)

        build_index(text)

        st.sidebar.success("PDF indexed successfully!")

    except Exception as e:

        st.sidebar.error(f"PDF error: {e}")



if "messages" not in st.session_state:

    st.session_state.messages = []



for msg in st.session_state.messages:

    st.chat_message(msg["role"]).write(msg["content"])



if prompt := st.chat_input("Ask me anything..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)



    context = retrieve(prompt)

    search_results = web_search(prompt) if use_search else ""



    full_prompt = prompt

    if context:

        full_prompt += f"\n\nDocument context:\n{context}"

    if search_results:

        full_prompt += f"\n\nWeb search results:\n{search_results}"



    messages = st.session_state.messages[:-1] + [{"role": "user", "content": full_prompt}]



    with st.spinner("Thinking..."):

        answer = get_response(messages, mode)



    st.session_state.messages.append({"role": "assistant", "content": answer})

    st.chat_message("assistant").write(answer)
