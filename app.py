import streamlit as st
import requests
import uuid

st.set_page_config(page_title="Agentic RAG", layout="wide")
st.title(" Smart Agent: PDF + Web + Memory")
st.caption("UI Connected to FastAPI Backend ")

BACKEND_URL = "http://127.0.0.1:550/ask"

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")
    st.write(f"**Session ID:** `{st.session_state.thread_id}`")
    
    if st.button("Clear Chat History"):
        st.session_state.thread_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me about the PDF or search the web..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    BACKEND_URL, 
                    params={"request": prompt}, 
                    timeout=60
                )
                
                if response.status_code == 200:
                    api_data = response.json()
                    answer = api_data.get("messages", "No response content received.")
                    
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Backend Error: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error(" Could not connect to Backend. Make sure main.py is running!")
            except Exception as e:
                st.error(f" An error occurred: {str(e)}")