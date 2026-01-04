from typing import Annotated, List, Union
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(".env")
from langchain_huggingface import HuggingFaceEmbeddings
from tools import web_search_tool
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
class GraphState(TypedDict):
    messages: Annotated[List, add_messages] 
    question: str
    generation: str
    documents: str

def retrieve_node(state, retriever):
    print("--- RETRIEVING FROM PDF ---")
    question = state["question"]
    docs = retriever.invoke(question)
    context = "\n".join([d.page_content for d in docs])
    return {"documents": context}

def web_search_node(state):
    print("--- WEB SEARCHING ---")
    question = state["question"]
    results = web_search_tool.invoke(question)
    if isinstance(results, str):
        return {"documents": results} 
    search_content = ""
    for res in results:
        if isinstance(res, dict) and 'content' in res:
            search_content += f"\nSource: {res.get('url', 'Unknown')}\nContent: {res['content']}\n"
        else:
            search_content += str(res) + "\n"    
    return {"documents": search_content}

def generator_node(state):
    print("--- GENERATING ANSWER WITH MEMORY ---")
    question = state["question"]
    context = state.get("documents", "No specific context found.")
    history = state["messages"] 

    prompt = f"""You are a helpful AI assistant. Use the conversation history and the context below to answer.
    Context: {context}
    History: {history}
    Question: {question}
    Answer:"""
    
    response = llm.invoke(prompt)
    return {"generation": response.content, "messages": [response]}

def router_node(state):
    print("--- AI ROUTING ---")
    question = state["question"]
    
    router_prompt = f"""You are an expert router. 
    Your job is to decide the best source to answer the user's question.
    
    Rules:
    1. If the question is about technical topics found in a document (like AI papers, transformers, specific technical details), use 'vectorstore'.
    2. If the question is a general greeting or small talk (like hi, hello, how are you), use 'direct'.
    3. If the question requires current events, news, or general knowledge NOT in a specific document, use 'web_search'.

    Question: {question}
    Answer only with one word: 'vectorstore', 'web_search', or 'direct'. No explanation."""

    response = llm.invoke(router_prompt)
    decision = response.content.strip().lower()

    if "vectorstore" in decision:
        return "vectorstore"
    elif "direct" in decision:
        return "direct"
    else:
        return "web_search"