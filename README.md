# 🛍️ Fashion Product Recommendation System using LLMs (RAG + GPT-4)

This project demonstrates a **Fashion Product Recommendation System** that leverages **Large Language Models (LLMs)**, **FAISS/ChromaDB**, and **Retrieval-Augmented Generation (RAG)** to provide intelligent, conversational recommendations for clothing and apparel.

---

## 🚀 Features

- 🧠 Uses **OpenAI GPT-4** to generate natural language recommendations
- 🔍 Integrates **FAISS** or **ChromaDB** for fast vector search over product descriptions
- 📦 Supports structured & unstructured data: titles, categories, descriptions, reviews
- 🎯 Enables **semantic search** and **chat-based recommendations**
- ⚙️ Built with modular architecture to support **RAG pipelines**
- 🔄 Scalable and customizable for any product catalog

---

## 🧩 Architecture Overview

```plaintext
        ┌────────────┐       ┌─────────────┐       ┌────────────┐
        │   User     │ ───►  │   GPT-4 LLM  │ ───►  │ RAG Engine │
        └────────────┘       └─────────────┘       └────┬───────┘
                                                        ▼
                                             ┌───────────────────┐
                                             │ Vector Store (FAISS│
                                             │ or ChromaDB)       │
                                             └───────────────────┘
                                                        ▲
                                              ┌──────────────┐
                                              │ Fashion Data │
                                              └──────────────┘
