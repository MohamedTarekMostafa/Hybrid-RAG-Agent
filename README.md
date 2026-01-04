# 🧠 Agentic RAG: Intelligent PDF & Web Assistant

An advanced, state-of-the-art **Agentic RAG** (Retrieval-Augmented Generation) system. Unlike traditional RAG pipelines, this system utilizes a **State Graph** architecture to dynamically route queries, manage long-term memory, and bridge the gap between static documents and the live internet.

---

## 🖼️ Project Visuals

### 1. Agent Workflow (LangGraph)
The logic of the agent is structured as a state machine. The router dynamically decides the execution path based on the user's intent.

![Agent Graph Structure](رابط_صورة_الجراف_هنا)


### 2. User Interface (Streamlit)
The interface allows for seamless PDF uploading, real-time chat, and history management.

| PDF Initialization | Web Search Interaction | Memory & Context |
| :---: | :---: | :---: |
| ![UI 1](رابط_صورة_الـUI_الأولى) | ![UI 2](رابط_صورة_الـUI_الثانية) | ![UI 3](رابط_صورة_الـUI_الثالثة) |

---

## 🏗️ System Architecture & Design Patterns

The project implements a **Decision-Making Agent** workflow using the following components:

### 🚀 Dynamic AI Routing (The Brain)
Instead of hard-coded rules, the agent uses **Llama 3.3-70B** to analyze user intent. It classifies queries into:
* **Vectorstore Route**: For deep-dive technical questions found in the uploaded PDF.
* **Web Search Route**: For real-time data, news, or general knowledge using **Tavily AI**.
* **Direct Route**: For conversational greetings and small talk.

### 🔄 State-Machine Orchestration (LangGraph)
The workflow is managed as a directed graph where each node represents a specific action (Retrieve, Search, Generate). This ensures:
* **Reliability**: Predictable transitions between different stages of the process.
* **Persistence**: Each session is assigned a `thread_id` to maintain context across multiple turns using `MemorySaver`.

---

## 📁 File Structure Deep-Dive

| File | Responsibility |
| :--- | :--- |
| `app.py` | **Frontend**: Streamlit UI, Session management, and Langfuse callback handlers. |
| `agent.py` | **Orchestration**: Graph definition, conditional edges, and state persistence. |
| `nodes.py` | **Execution**: Logic for AI Routing, Web Searching, and LLM Generation. |
| `tools.py` | **Infrastructure**: PDF loading, text splitting (Recursive), and Vectorstore setup. |

---
