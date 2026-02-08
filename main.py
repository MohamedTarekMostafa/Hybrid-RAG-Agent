from fastapi import FastAPI
from agent import create_graph
from tools import get_retriever
from langfuse.langchain import CallbackHandler
from dotenv import load_dotenv
pdf_path = 'attention_is_all_you_need.pdf'
retriever = get_retriever(pdf_path)
load_dotenv(".env")
langfuse_handler = CallbackHandler()
config = {"configurable":{"thread_id":"1"},"callbacks":[langfuse_handler]}
bot  = create_graph(retriever)
app  = FastAPI()
@app.post("/ask")
async def get_data(request:str):
    inputs = {"question":request}
    response = bot.invoke(inputs,config)
    final_message = response['messages'][-1].content
    return {"messages":final_message}

