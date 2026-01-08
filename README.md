#  Agentic RAG: The Intelligent PDF & Web Assistant

Building a standard RAG system was a great start, but I wanted something that doesn't just "retrieve"—I wanted a system that **thinks**. 

This project is the **Agentic evolution** of my previous work. While my [Traditional RAG Project](https://github.com/MohamedTarekMostafa/Pay-Attention-The-Transformer-RAG) was focused on pinpointing data within a specific paper, this **Agentic RAG** takes it to the next level by using a **State Graph** architecture to navigate between static documents and the live internet.

---

##  Why go Agentic? (Agentic vs. Traditional)

You might wonder, why not stick to the traditional pipeline? After building the [Pay-Attention RAG](https://github.com/MohamedTarekMostafa/Pay-Attention-The-Transformer-RAG), I noticed a few gaps that only an "Agent" could bridge:

* **Dynamic Routing:** Traditional RAG always looks at the vectorstore. This system *decides* if it needs the PDF, a Google search (via Tavily), or just a friendly chat.
* **Self-Correction:** Unlike static chains, an Agentic flow can evaluate its own path. If the data isn't in the PDF, it doesn't give up—it switches to the web.
* **Contextual Memory:** Using `thread_id` and `MemorySaver`, this system remembers our conversation history, making it feel like a real research partner rather than a search engine.

---

##  Project Visuals & Workflow

### 1. Agent Logic (LangGraph)
The "Core Point" of this project isn't a straight line; it's a state machine. The router analyzes your intent and maps out the best path for the answer.

![Agent Workflow](https://github.com/user-attachments/assets/6f6a908c-1ff7-4dc3-8690-8e1849e936ec)



---

##  System Architecture

I designed this agent to act as a **Decision-Maker** using a few core pillars:

###  Dynamic AI Routing
Powered by **Llama 3.3-70B**, the agent classifies your query on the fly:
* **Vectorstore Route**: For deep technical dives into your uploaded documents.
* **Web Search Route**: For real-time data or general knowledge using **Tavily AI**.
* **Direct Route**: For those quick greetings and casual conversation.

### 🔄 State-Machine Orchestration
Using **LangGraph**, I’ve structured the logic into a directed graph. This ensures the process is:
* **Reliable:** Predictable transitions between nodes (Retrieve -> Generate).
* **Persistent:** It stays in sync with our conversation using persistent checkpoints.

---

## 📁 Inside the Codebase

| File | What's inside? |
| :--- | :--- |
| `app.py` | The **Streamlit UI** and session management logic. |
| `agent.py` | The **Orchestration** layer where the Graph and edges live. |
| `nodes.py` | The **Action** logic (Routing, Searching, Generating). |
| `tools.py` | The **Infrastructure** (PDF loading and Vectorstore setup). |

---

##  Interface & Experience

In this section, you can see how the agent handles different types of queries, from technical PDF analysis to live web updates.

*(Add your screenshots below to showcase the UI in action)*

### 1. The Dashboard
> [Insert Screenshot of the main UI here]

### 2. Multi-Turn Conversation
> [Insert Screenshot showing how it remembers previous questions here]

### 3. Web Search Integration
> [Insert Screenshot of a web-based answer here]

---

## 🚀 Getting Started

1.  **Clone the repo** and install dependencies.
2.  Set up your `.env` with **Groq**, **Tavily**, and **Google** API keys.
3.  Run the app: `streamlit run app.py`

*Always looking to improve the logic! If you have thoughts on Agentic workflows, let's talk.*

