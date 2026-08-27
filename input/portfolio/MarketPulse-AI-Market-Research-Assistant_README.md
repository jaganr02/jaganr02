# 🚀 MarketPulse AI

> Autonomous Multi-Agent Competitive Intelligence & Market Research Engine powered by LangGraph, FastAPI, Qdrant, Google Gemini, and Docker.

---

## 📖 Overview

MarketPulse AI is a production-ready multi-agent AI platform that autonomously performs market research, competitor intelligence, and business analysis.

The platform uses multiple AI agents orchestrated with LangGraph to search, analyze, critique, and summarize market information while storing knowledge inside a vector database for future retrieval.

---

# ✨ Features

- 🤖 Multi-Agent AI Workflow
- 🔍 Autonomous Web Research
- 📚 Vector Database Integration (Qdrant)
- 🧠 Google Gemini Embeddings
- 📄 AI-generated Research Reports
- ⚡ FastAPI REST APIs
- 🌐 Server-Sent Events (SSE) Streaming
- 🐳 Dockerized Production Deployment
- ❤️ Health Check Endpoint
- 📦 Multi-stage Docker Build
- 🔒 Non-root Container Execution

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
              FastAPI Backend
                      │
                      ▼
               LangGraph Workflow
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
Research Agent   Critic Agent   Writer Agent
      │
      ▼
   Tavily Search API
      │
      ▼
 Google Gemini Embeddings
      │
      ▼
 Qdrant Vector Database
      │
      ▼
 AI Generated Report
```

---

# 🧩 AI Agents

## 🔍 Research Agent

Responsibilities

- Searches the web using Tavily
- Collects relevant sources
- Splits content into chunks
- Generates embeddings
- Stores knowledge in Qdrant

---

## 🧠 Critic Agent

Responsibilities

- Reviews research quality
- Detects insufficient evidence
- Validates collected information
- Decides approval or rejection

---

## ✍️ Writer Agent

Responsibilities

- Generates final research summary
- Creates structured report
- Produces business-ready output

---

# ⚙️ Tech Stack

## Backend

- Python 3.11
- FastAPI
- Uvicorn

## AI Framework

- LangGraph
- LangChain Text Splitters

## LLM

- Google Gemini

## Search

- Tavily Search API

## Vector Database

- Qdrant

## Communication

- SSE (Server Sent Events)

## Deployment

- Docker
- Docker Compose

---

# 📂 Project Structure

```
MarketPulse AI/

│
├── backend/
│   ├── app/
│   │
│   ├── api/
│   ├── config/
│   ├── core/
│   │   ├── agents/
│   │   ├── llm/
│   │   ├── memory/
│   │   ├── prompts/
│   │   ├── reflection/
│   │   ├── retrieval/
│   │   └── database.py
│   │
│   ├── services/
│   ├── schemas/
│   ├── middleware/
│   ├── models/
│   └── utils/
│
├── frontend/
│
├── deployment/
│   ├── docker/
│   └── nginx/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/MarketPulse-AI.git

cd MarketPulse-AI
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

---

# ▶️ Run Locally

```bash
python -m uvicorn backend.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# 🐳 Docker Deployment

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

# 🌐 API Endpoints

## Home

```
GET /
```

---

## Health Check

```
GET /health
```

---

## Streaming Research

```
GET /api/v1/research/stream?query=AI startups
```

---

# 🗄️ Qdrant Dashboard

```
http://localhost:6333/dashboard
```

---

# 🔄 Workflow

```
User Query
     │
     ▼
Research Agent
     │
     ▼
Tavily Search
     │
     ▼
Chunk Documents
     │
     ▼
Gemini Embeddings
     │
     ▼
Store in Qdrant
     │
     ▼
Critic Agent
     │
     ▼
Writer Agent
     │
     ▼
Final Research Report
```

---

# 🧪 Testing

Run all tests

```bash
python scripts/test_graph.py

python scripts/test_qdrant.py

python scripts/test_research_agent.py

python scripts/test_critic_agent.py
```

---

# 📈 Current Status

| Module | Status |
|---------|--------|
| Frontend UI | ✅ |
| FastAPI Backend | ✅ |
| LangGraph Workflow | ✅ |
| Research Agent | ✅ |
| Critic Agent | ✅ |
| Writer Agent | ✅ |
| Google Gemini | ✅ |
| Tavily Search | ✅ |
| Qdrant Integration | ✅ |
| Docker Deployment | ✅ |
| Docker Compose | ✅ |
| Health Check | ✅ |

---

# 🔮 Future Improvements

- Authentication
- User Accounts
- Research History
- PDF Export
- Report Download
- Citation Generator
- Redis Cache
- PostgreSQL
- Kubernetes Deployment
- CI/CD Pipeline
- Monitoring
- Prometheus
- Grafana
- OpenTelemetry
- LangSmith Observability

---

# 👨‍💻 Author

**R Jagan**

B.Tech Artificial Intelligence & Data Science

AI Engineer | Generative AI | Multi-Agent Systems | RAG | FastAPI | LangGraph

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

- Google Gemini
- LangGraph
- LangChain
- Tavily
- Qdrant
- FastAPI
- Docker