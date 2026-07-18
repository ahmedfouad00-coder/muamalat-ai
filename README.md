# Muamalat AI | معاملات AI

**An AI-powered assistant for Islamic financial jurisprudence (Fiqh al-Muamalat).**

An end-to-end Retrieval-Augmented Generation (RAG) system that answers Islamic finance questions using verified fatwas. The system combines semantic search with ChromaDB, HuggingFace Embeddings, and Groq LLMs to generate accurate, source-grounded responses through a FastAPI backend.

<p align="center">
  <img src="img/Archtecture.png" alt="Muamalat AI Architecture" width="900"/>
</p>

## Project Demo

Watch the project demonstration on YouTube:

**https://youtu.be/eDT6bg_Um9c?si=eTSATjzD5W6vsk4q**

---

## Features

- End-to-End RAG Pipeline
- Semantic Search with ChromaDB
- HuggingFace Embeddings (BAAI/bge-m3)
- Groq LLM Integration
- Multi-Agent Architecture
- FastAPI REST API
- Prompt Engineering
- Automated Evaluation Pipeline
- Source-Grounded Responses

---

## Project Structure

```text
app/
│
├── Agents/          # AI agents
├── api/             # FastAPI endpoints
├── evaluation/      # Evaluation pipeline
├── prompts/         # Prompt templates
├── rag/             # Retrieval pipeline
├── static/          # Frontend assets
├── templates/       # HTML templates
└── main.py          # FastAPI entry point
```

---

## Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- HuggingFace Transformers
- BAAI/bge-m3 Embeddings
- Groq API

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/muamalat-ai.git
cd muamalat-ai
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Dataset

The knowledge base consists of verified Islamic finance fatwas stored in JSON format and indexed into ChromaDB for semantic retrieval.

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

Open the application:

- **API:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs

---

## Evaluation

The project includes an evaluation pipeline to assess the quality of generated answers against the retrieved context.

---

## Retrieval Pipeline

1. User submits a question.
2. The query is converted into embeddings.
3. ChromaDB retrieves the most relevant fatwas.
4. Retrieved context is injected into the prompt.
5. Groq LLM generates a grounded response.

---

## Contact

If you have any questions or suggestions, feel free to open an issue or connect with me on LinkedIn.

- **LinkedIn:** https://www.linkedin.com/in/ahmed-fouad-182186376
