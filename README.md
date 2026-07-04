# AWOS - Autonomous Workforce Operating System

> **An AI workforce, not just an AI assistant.**

AWOS is a multi-agent AI platform built for the **Slack Agent Builder Challenge 2026**. Instead of relying on a single AI assistant, AWOS dynamically creates specialized AI agents that collaborate, communicate, and complete complex tasks inside Slack using **Model Context Protocol (MCP)**.

---

## 🚀 Overview

AWOS transforms Slack into an intelligent workspace where AI agents function like a real team.

A user provides a high-level objective, and AWOS:

- Analyzes the request
- Creates the required AI specialists
- Assigns responsibilities
- Coordinates collaboration
- Uses MCP to access external tools
- Delivers the final result in Slack

---

## ✨ Features

- 🤖 Dynamic AI Agent Creation
- 👥 Multi-Agent Collaboration
- 🧠 AI Debate & Decision Making
- 📌 Human Approval Workflow
- 💾 Shared Project Memory
- 📊 Live Progress Tracking
- 🔍 Explainable AI Decisions
- 🔗 Secure MCP Tool Integration

---

## 🏗️ Architecture

```text
                Slack Workspace
                       │
                Slack Bolt App
                       │
                AWOS Orchestrator
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    Agent Factory   Memory      Workflow Engine
        │
 ┌──────┼─────────────────────────────┐
 │      │        │        │          │
CEO     PM   Research  Engineer      QA
        │
        ▼
      MCP Client
        │
      MCP Server
        │
 ┌──────┼───────────────┬──────────────┐
 │      │               │              │
GitHub SQLite      Python Tools   File System
```

---

## 🛠️ Tech Stack

### Backend

- Python 3.11+
- FastAPI
- Uvicorn

### Slack

- Slack Bolt SDK
- Slack SDK
- Block Kit

### AI

- Google Gemini API (Free Tier)
- LangGraph (or Custom Agent Orchestrator)

### MCP

- Model Context Protocol (Python SDK)

### Database

- SQLite

### Version Control

- Git & GitHub

---

## 📂 Project Structure

```text
AWOS/
│
├── app/
│   ├── agents/
│   ├── orchestrator/
│   ├── slack/
│   ├── mcp/
│   ├── database/
│   ├── utils/
│   ├── config.py
│   └── main.py
│
├── docs/
├── demo/
├── tests/
├── requirements.txt
├── README.md
├── .env.example
└── docker-compose.yml
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/AWOS.git
cd AWOS
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
SLACK_BOT_TOKEN=
SLACK_APP_TOKEN=
SLACK_SIGNING_SECRET=

GOOGLE_API_KEY=

DATABASE_URL=sqlite:///awos.db
```

---

## ▶️ Run the Project

Start FastAPI

```bash
uvicorn app.main:app --reload
```

Start the Slack app

```bash
python app/slack/app.py
```

Start the MCP Server

```bash
python app/mcp/server.py
```

---

## 💡 Example Workflow

**User Input**

> Build an AI-powered healthcare application.

AWOS automatically:

1. Creates a CEO Agent
2. Creates a Project Manager
3. Creates a Research Agent
4. Creates an Engineer
5. Creates a QA Reviewer
6. Uses MCP tools to gather information
7. Coordinates all agents
8. Delivers the final proposal in Slack

---

## 📅 Development Timeline

| Day | Goal                                   |
| --- | -------------------------------------- |
| 1   | Project setup, Slack app, MCP skeleton |
| 2   | AWOS Orchestrator & Agent Factory      |
| 3   | Core AI Agents                         |
| 4   | MCP Tool Integration                   |
| 5   | Agent Communication                    |
| 6   | Memory & Approval Workflow             |
| 7   | Block Kit UI & Progress Dashboard      |
| 8   | Testing & Bug Fixes                    |
| 9   | Demo Video & Final Submission          |

---

## 👥 Team

| Module                        | Owner         |
| ----------------------------- | ------------- |
| Slack UI & Integration        | Team Member 1 |
| AWOS Orchestrator & Agents    | Team Member 2 |
| MCP Server & Tools            | Team Member 3 |
| Testing, Documentation & Demo | Team Member 4 |

---

## 🎯 Hackathon

**Slack Agent Builder Challenge 2026**

**Track:** New Slack Agent

**Primary Technology:** Model Context Protocol (MCP)

---

## 🌟 Vision

AWOS is more than a chatbot—it is an **Autonomous Workforce Operating System** where intelligent AI agents collaborate like a real team to solve complex problems. By combining Slack, MCP, and multi-agent orchestration, AWOS demonstrates a possible future of enterprise collaboration.

---

## 📄 License

This project is developed for the **Slack Agent Builder Challenge 2026**.

```

```
