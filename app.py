import os
import operator
from typing import TypedDict, Annotated, Sequence

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.runnables import RunnablePassthrough
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langgraph.graph import StateGraph, END

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

model = ChatOpenAI(model="gpt-4o", temperature=0.2)
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

loader = TextLoader("project_data.txt")  # Adjust path if needed
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=150)
docs = text_splitter.split_documents(documents=docs)
docs = [doc for doc in docs if doc.page_content.strip() != ""]
if len(docs) == 0:
    raise ValueError("No documents to embed. Check your input file or splitting logic.")

db = Chroma.from_documents(docs, embedding_model)
retriever = db.as_retriever(search_kwargs={"k": 3})

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

class TopicSelectionParser(BaseModel):
    Topic: str = Field(description="Selected Topic")
    Reasoning: str = Field(description="Reasoning behind the topic selection")

parser = PydanticOutputParser(pydantic_object=TopicSelectionParser)

def function1(state):
    messages = state["messages"]
    question = messages[-1].content
    template = """
    Your task is to classify the given user query into one of the following categories: ["fever", "cough", "rash", "pain", "vomiting", "headache", "fatigue", "shortness", "breathing", 
    "sore", "chills", "dizziness", "sweating", "itchy", "diarrhea", "urination", "sadness", 
    "insomnia", "jaundice", "abdominal", "joint", "anxiety", "depression", "appetite", not related].
    Only respond with the category name and nothing else.
    User Query: {question}
    {format_instructions}
    """
    prompt = ChatPromptTemplate.from_template(template).partial(
        format_instructions=parser.get_format_instructions()
    )
    chain = prompt | model | parser
    result = chain.invoke({"question": question})
    return {"messages": messages}

def function2(state):
    messages = state["messages"]
    question = messages[-1].content
    template = """
    Answer the question using ONLY the following context:
    {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    retrieval_chain = prompt | model
    docs = retriever.invoke(question)
    context = "\n".join([doc.page_content for doc in docs])
    response = retrieval_chain.invoke({"context": context, "question": question})
    return {"messages": [HumanMessage(content=response.content)]}

def function3(state):
    messages = state["messages"]
    question = messages[-1].content
    full_prompt = f"Answer the following question using your own knowledge:\n{question}"
    response = model.invoke(full_prompt)
    return {"messages": [HumanMessage(content=response.content)]}

def router(state):
    messages = state["messages"]
    question = messages[-1].content.lower()
    if "diseases" in question:
        return "RAGcall"
    else:
        return "LLMcall"

workflow = StateGraph(AgentState)
workflow.add_node("agent", function1)
workflow.add_node("LLMcall", function3)
workflow.add_node("RAGcall", function2)
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", router, {
    "RAGcall": "RAGcall",
    "LLMcall": "LLMcall"
})
workflow.add_edge("RAGcall", END)
workflow.add_edge("LLMcall", END)
app_graph = workflow.compile()

st.set_page_config(page_title="Medical Query Assistant", layout="wide")
st.title("🩺 Medical Query Classifier & Assistant")

user_input = st.text_input("Enter your medical-related query:")

if st.button("Submit") and user_input:
    with st.spinner("Processing..."):
        try:
            result = app_graph.invoke({"messages": [HumanMessage(content=user_input)]})
            st.success("Response:")
            st.markdown(result["messages"][-1].content)
        except Exception as e:
            st.error(f"Error: {e}")
