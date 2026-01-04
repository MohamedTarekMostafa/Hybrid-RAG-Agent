
import streamlit as st
import os
from dotenv import load_dotenv
from tools import get_retriever
from agent import create_graph
from langfuse.langchain import CallbackHandler

load_dotenv('.env') 

langfuse_handler = CallbackHandler()

st.set_page_config(page_title="Agentic RAG with Langfuse", layout="wide")
st.title("🧠 Smart Agent: PDF + Web + Memory")
st.caption("Monitoring enabled via Langfuse 🚀")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_session_01"

uploaded_file = st.sidebar.file_uploader("Upload your Reference PDF", type="pdf")

if uploaded_file:
    with open("temp_document.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if "graph" not in st.session_state:
        with st.spinner("Initializing Vector Database..."):
            retriever = get_retriever("temp_document.pdf")
            st.session_state.graph = create_graph(retriever)
        st.sidebar.success("System is Ready & Tracing Active!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me about the PDF or search the web..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                config = {
                    "configurable": {"thread_id": st.session_state.thread_id},
                    "callbacks": [langfuse_handler], 
                    "run_name": f"Agent_Run_{st.session_state.thread_id}"
                }
                
                inputs = {
                    "question": prompt,
                    "messages": [("user", prompt)]
                }
                
                try:
                    result = st.session_state.graph.invoke(inputs, config=config)
                    response = result.get("generation", "I couldn't process that.")
                    
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
                except Exception as e:
                    st.error(f"Error during execution: {str(e)}")

if st.sidebar.button("Clear Chat History"):
    st.session_state.thread_id = os.urandom(4).hex() 
    st.session_state.messages = []
    st.rerun()




