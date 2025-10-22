# FAQ Agent – LangChain-Powered Agentic FAQ Assistant

![LangChain](https://img.shields.io/badge/langchain-%230096ff.svg?style=flat&logo=langchain&logoColor=white)
![FastAPI](https://img.shields.io/badge/fastapi-0.119.0-brightgreen)
![OpenAI](https://img.shields.io/badge/OpenAI-API-blue)

> Agentic FAQ system built with LangChain, OpenAI, and FastAPI – designed to answer business-specific questions using context-aware tools and RAG pipelines.

---

## Features

- **Tool-augmented LangChain Agent** with `SearchFAQ`
- **Context-aware RAG retrieval** using vector similarity (FAISS)
- **OpenAI-powered function agents** with dynamic prompting
- **Cited sources** returned with every answer
- **Upload endpoint** to ingest new documents
-  Built with **FastAPI** and served via **Uvicorn**

---

## Architecture Overview

See [`AGENTIC_ARCHITECTURE.md`](./AGENTIC_ARCHITECTURE.md) for full flow diagram and agent breakdown.

User Query
▼
FastAPI (/ask)
▼
LangChain Agent (OpenAI Functions Agent)
└── Tool: SearchFAQ
└── Vectorstore RAG (Top-K Chunks)
└── Formatted Prompt
▼
LLM Response + Sources

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/SBathio/faq-agent.git
cd faq-agent

2. Set Up Environment

cp .env.example .env
# Edit .env to add your OpenAI key and model name

3. Install Dependencies

pip install -r requirements.txt

4. Run the Server

uvicorn main:app --reload

	•	Visit the API: http://127.0.0.1:8000/docs

⸻

API Endpoints

POST /ask

Ask a question using the agentic flow.

Request:

{
  "query": "What is the refund policy?",
  "style": "default"
}

Response:

{
  "query": "What is the refund policy?",
  "answer": "You can request a refund within 30 days...",
  "sources": [
    {
      "source": "refund_policy.txt",
      "content": "To request a refund, email support..."
    }
  ]
}


⸻

POST /upload

Upload documents to enrich the agent’s knowledge.

Form field: file

⸻

Tech Stack

Layer	Technology
Backend	FastAPI + Uvicorn
AI Engine	LangChain Agents
LLM	OpenAI GPT-4 / GPT-3.5
RAG Backend	FAISS (local vector DB)
Tools	Custom LangChain Tool
Prompting	LangChain Hub + Dynamic Templates


⸻

Agent Details
	•	Agent Type: create_openai_functions_agent()
	•	Prompt Source: langchainhub: hwchase17/openai-functions-agent
	•	Tool Name: SearchFAQ
	•	LLM Config: Controlled via .env

⸻

Project Structure

faq-agent/
├── agent/
│   ├── agent_executor.py   ← LangChain Agent setup
│   └── faq_agent.py        ← Wrapper for API access
├── api/
│   ├── routes.py           ← /ask route
│   └── upload.py           ← /upload route
├── rag/
│   └── retriever.py        ← Top-K chunk retrieval
├── models/
│   └── prompt_template.py  ← Prompt styles
├── utils/
│   └── config.py           ← Env loader
├── .env.example
├── requirements.txt
├── main.py
└── README.md


⸻

Credits

Built by SBathio – LangChain + OpenAI developer | Ph.D. AI | Cloud-Native Architect

⸻

License

MIT License – see LICENSE file.

⸻

Coming Soon
	• Conversational memory support
	• Multi-modal input (voice/image)
	• Agentic workflow orchestration with LangGraph
	• Custom multi-tool chains (e.g., Web Search, SQL)

⸻

Empower your customer service with LLMs. This is not just RAG — it’s Agentic Intelligence.