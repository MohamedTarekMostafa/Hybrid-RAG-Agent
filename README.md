![WhatsApp Image 2026-01-04 at 5 00 41 PM](https://github.com/user-attachments/assets/ccacf2b8-34bd-4a9a-b6bb-bc869dd51e8e)# 🧠 Agentic RAG: Intelligent PDF & Web Assistant

An advanced, state-of-the-art **Agentic RAG** (Retrieval-Augmented Generation) system. Unlike traditional RAG pipelines, this system utilizes a **State Graph** architecture to dynamically route queries, manage long-term memory, and bridge the gap between static documents and the live internet.

---

## 🖼️ Project Visuals

### 1. Agent Workflow (LangGraph)
The logic of the agent is structured as a state machine. The router dynamically decides the execution path based on the user's intent.

![Agent Graph Structure](![WhatsApp Image 2026-01-04 at 5 00 41 PM](https://github.com/user-attachments/assets/6f6a908c-1ff7-4dc3-8690-8e1849e936ec))


### 2. User Interface (Streamlit)
The interface allows for seamless PDF uploading, real-time chat, and history management.

![WhatsApp Image 2026-01-04 at 6 40 34 PM](https://github.com/user-attachments/assets/e999b540-89d7-48f5-b6c3-02b1adf199b1)
![WhatsApp Image 2026-01-04 at 11 02 03 PM](https://github.com/user-attachments/assets/e174da9d-6aec-40f5-8c0d-c0fafc53a6cb)
![WhatsApp Image 2026-01-04 at 11 02 03 PM](https://github.com/user-attachments/assets/0c611d08-6919-4226-86e5-e4d35f326247)
![WhatsApp Image 2026-01-04 at 11 02 37 PM](https://github.com/user-attachments/assets/68f5e4f6-d702-495b-9afa-4ad071343a60)


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

