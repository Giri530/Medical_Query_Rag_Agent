Hybrid AI Chatbot – LLM + RAG Powered:
This is an intelligent chatbot built using Streamlit, LangChain, and LangGraph, capable of switching between a Large Language Model (LLM) and a Retrieval-Augmented Generation (RAG) pipeline based on the user’s query type.

Features
-> Hybrid Query Routing: Dynamically decides whether to use RAG or LLM based on input.

-> LLM Integration: Uses GPT-4o via OpenAI for general-purpose reasoning and chat.

-> RAG Pipeline: Retrieves relevant information from a domain-specific knowledge base (e.g., healthcare) using ChromaDB.

->LangGraph Workflow: Utilizes LangGraph for visual and conditional execution of chatbot flow.

-> Fast UI: Built with Streamlit for a lightweight, interactive web interface.

🛠️ Tech Stack
Tool	Purpose
Python	Core programming language
Streamlit	Web interface for the chatbot
OpenAI GPT-4o	Large Language Model for responses
HuggingFace	Embeddings for document retrieval
ChromaDB	Vector store for RAG
LangChain	Framework for chaining LLM tasks
LangGraph	Flow logic and routing engine

🚀 How It Works
User asks a question via the Streamlit UI.

The backend routes the question using LangGraph:

If it’s related to known topics (like “LangGraph”, “Agent AI”, etc.), it uses RAG.

Otherwise, it uses LLM for free-form answers.

The selected path executes and returns a response to the user.

📂 Folder Structure
Hybridbot/
│
├── app.py             #Main application with Streamlit UI and full LangChain + LangGraph logic
├── healthcare.txt     # Knowledge base for RAG
├── requirements.txt   # Python dependencies
└── .env               # Stores OpenAI API key
📄 Setup Instructions
git clone https://github.com/Giri530/hybrid-ai-chatbot.git
cd hybrid-ai-chatbot
Install dependencies:
pip install -r requirements.txt
Add our OpenAI API key in a .env file:
OPENAI_API_KEY=your_openai_key_here
Run the chatbot:
streamlit run app.py
