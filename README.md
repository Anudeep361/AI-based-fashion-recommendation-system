# 🛍️ Fashion Product Recommendation System using LLMs (RAG + GPT-4 + Streamlit)

This project showcases a **chat-based fashion recommender system** using **Large Language Models (LLMs)** and **semantic search** powered by **FAISS** or **ChromaDB**, combined with a **Streamlit UI** for easy deployment and interaction.

---

## 🚀 Features

- 🤖 GPT-4 powered chat interface for natural product discovery
- 🔍 Semantic product search using **FAISS** or **ChromaDB**
- 🧠 Retrieval-Augmented Generation (RAG) to improve accuracy and context
- 🛒 Designed for **fashion products** (clothing, shoes, accessories)
- 🖥️ Deployed via **Streamlit** for interactive web-based exploration

---

## 🧩 Architecture

```plaintext
        ┌────────────┐       ┌─────────────┐       ┌────────────┐
        │   User     │ ───►  │ Streamlit UI│ ───►  │ GPT-4 (LLM)│
        └────────────┘       └────┬────────┘       └────┬───────┘
                                  ▼                        ▼
                         ┌────────────────┐     ┌───────────────────┐
                         │ RAG Retriever  │◄───►│ FAISS / ChromaDB  │
                         └────────────────┘     └───────────────────┘
