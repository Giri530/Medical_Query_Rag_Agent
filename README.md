# 🤖 Hybrid AI Chatbot — LLM + RAG Powered

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai" />
  <img src="https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20Store-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LangGraph-Routing-blueviolet?style=for-the-badge" />
</p>

<p align="center">
  An intelligent chatbot that <strong>dynamically switches</strong> between a Large Language Model and a RAG pipeline<br/>
  based on the user's query — built with Streamlit, LangChain, and LangGraph.
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [Usage](#-usage)
- [Contributing](#-contributing)

---

## 🔍 Overview

The **Hybrid AI Chatbot** combines the power of **GPT-4o** for general reasoning with a **Retrieval-Augmented Generation (RAG)** pipeline for domain-specific queries. A LangGraph-based router intelligently decides which path to take — ensuring accurate, context-aware responses every time.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔀 **Hybrid Query Routing** | Dynamically routes to RAG or LLM based on query type |
| 🧠 **LLM Integration** | GPT-4o via OpenAI for general-purpose reasoning |
| 📚 **RAG Pipeline** | Retrieves from a domain-specific knowledge base using ChromaDB |
| 🔗 **LangGraph Workflow** | Visual & conditional execution of chatbot flow |
| ⚡ **Fast UI** | Lightweight, interactive web interface via Streamlit |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web interface for the chatbot |
| **OpenAI GPT-4o** | LLM for general-purpose responses |
| **HuggingFace** | Embeddings for document retrieval |
| **ChromaDB** | Vector store for RAG |
| **LangChain** | Framework for chaining LLM tasks |
| **LangGraph** | Flow logic and conditional routing engine |

---

## 🔄 How It Works

```
User Question (Streamlit UI)
         │
         ▼
 ┌───────────────────┐
 │   LangGraph Router │
 └────────┬──────────┘
          │
    ┌─────┴──────┐
    │            │
    ▼            ▼
 RAG Path     LLM Path
 (ChromaDB    (GPT-4o
  + HF Emb)   General)
    │            │
    └─────┬──────┘
          │
          ▼
     Response to User
```

1. User asks a question via the **Streamlit UI**
2. **LangGraph** routes the query:
   - Known domain topics (e.g., healthcare, LangGraph, Agent AI) → **RAG pipeline**
   - General / open-ended questions → **GPT-4o LLM**
3. The selected path executes and returns a response

---

## 📁 Project Structure

```
hybrid-ai-chatbot/
├── app.py              # Main app — Streamlit UI + LangChain + LangGraph logic
├── healthcare.txt      # Knowledge base for RAG
├── requirements.txt    # Python dependencies
└── .env                # Stores OpenAI API key (not committed)
```

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Giri530/hybrid-ai-chatbot.git
cd hybrid-ai-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key_here
```

### 4. Run the Chatbot

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser 🎉

---

## 💬 Usage

- Ask a **domain-specific question** (e.g., healthcare) → RAG pipeline kicks in, retrieves from `healthcare.txt`
- Ask a **general question** (e.g., "Explain transformers") → GPT-4o responds directly
- The routing happens **automatically** — no manual switching needed

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
# Open a Pull Request
```

---

<p align="center">
  <strong>Made with ❤️ by Girinath &nbsp;·&nbsp; Powered by LangChain, LangGraph & GPT-4o</strong>
</p>
