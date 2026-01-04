from langgraph.graph import END, StateGraph
from langgraph.checkpoint.memory import MemorySaver 
from nodes import retrieve_node, web_search_node, generator_node, router_node, GraphState
from dotenv import load_dotenv
load_dotenv(".env")
def create_graph(retriever):
    workflow = StateGraph(GraphState)
    checkpoint_memory = MemorySaver() 

    workflow.add_node("retriever", lambda state: retrieve_node(state, retriever))
    workflow.add_node("web_search", web_search_node)
    workflow.add_node("generate", generator_node)

    workflow.set_conditional_entry_point(
        router_node,
        {
            "vectorstore": "retriever",
            "web_search": "web_search",
            "direct": "generate",
        },
    )

    workflow.add_edge("retriever", "generate")
    workflow.add_edge("web_search", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile(checkpointer=checkpoint_memory)