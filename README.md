# 🚀 AWOS - Autonomous Workforce Operating System

> Transforming Slack into an AI-powered autonomous workforce using Multi-Agent AI, FastAPI, LangGraph, Gemini, and Model Context Protocol (MCP).

---
# Demo Link
https://youtu.be/i-6P13aRaIs?si=I0wmR2cbZ8rFpxPt

---

# 📌 Overview

AWOS (Autonomous Workforce Operating System) is an AI-powered multi-agent platform that enables users to accomplish complex tasks by simply providing a goal in Slack.

Instead of relying on a single chatbot, AWOS dynamically creates specialized AI agents such as a CEO, Project Manager, Researcher, Engineer, and QA Reviewer. These agents collaborate, delegate work, communicate with external tools through MCP, and deliver a complete solution while keeping the user involved through approval checkpoints.

---

# ❗ Problem Statement

Traditional AI assistants perform isolated tasks but cannot collaborate like a real workforce.

Modern software development requires multiple specialists working together, coordinating tasks, accessing external tools, and making collaborative decisions.

AWOS solves this problem by creating an autonomous AI workforce capable of planning, reasoning, executing, and validating tasks collaboratively inside Slack.

---

# ✅ Solution

When a user submits a request in Slack, AWOS performs the following workflow:

1. Receives the user request.
2. Creates a new mission.
3. Analyzes the objective.
4. Classifies the task.
5. Uses Gemini AI for reasoning and planning.
6. Generates an execution workflow using LangGraph.
7. Creates specialized AI agents.
8. Connects to external tools through MCP.
9. Collects results.
10. Sends the final response back to Slack.

---

# 🏗 System Architecture

```text
                     User
                       │
                       ▼
                  Slack Workspace
                       │
                       ▼
                Slack Application
                       │
                       ▼
                 AWOS Core API
                       │
                       ▼
                  Mission Pipeline
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    Analyzer      Classifier     Planner
                       │
                       ▼
              Gemini Reasoning Engine
                       │
                       ▼
                LangGraph Workflow
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      CEO          Researcher      Engineer
                       │
                       ▼
                 GitHub MCP Server
                       │
                       ▼
                  GitHub Services
                       │
                       ▼
                  QA Validation
                       │
                       ▼
                 Response to Slack
```

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI

## Artificial Intelligence

- Google Gemini API
- LangGraph

## Communication

- Slack Bolt SDK
- Slack Block Kit

## External Tool Integration

- Model Context Protocol (MCP)

## Database

- SQLite

## Version Control

- Git
- GitHub

---

# 📁 Repository Structure

```text
AWOS/
│
├── awos-core/
├── slack-app/
├── mcp-server/
├── docs/
├── tests/
├── assets/
├── scripts/
├── .gitignore
├── LICENSE
└── README.md
```

---

# 📦 Modules

## AWOS Core

Responsible for:

- FastAPI Backend
- Mission API
- Analyzer
- Classifier
- Planner
- Gemini Integration
- LangGraph Workflow
- AI Agent Orchestration

---

## Slack Application

Responsible for:

- Slack Commands
- Slack Events
- User Messages
- Approval Buttons
- Slack UI

---

## GitHub MCP Server

Responsible for:

- GitHub Authentication
- Repository Management
- File Management
- Pull Requests
- MCP Tool APIs

---

## Documentation & QA

Responsible for:

- Project Documentation
- Architecture Documentation
- User Guide
- API Documentation
- Testing
- Bug Reports
- Demo Preparation
- Presentation

---

# 👥 Team Members

| Name       | Role                                        |
| ---------- | ------------------------------------------- |
| Johney     | AWOS Core Architect & AI Orchestration Lead |
| Lokesh     | Slack Integration Developer                 |
| Manaswitha | GitHub MCP Developer                        |
| Devaj      | Documentation & QA Engineer                 |

---

### 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Project-AWOS/AWOS.git
```

---

### Backend Setup

Navigate to the backend:

```bash
cd AWOS/awos-core
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the backend:

```bash
python app/main.py
```

or

```bash
python -m uvicorn app.main:app --reload
```

---

### Slack App Setup

Open a new terminal and navigate to the Slack application:

```bash
cd AWOS/slack-app
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the Slack application:

```bash
python app.py
```

---

### Running the System

To use AWOS end-to-end, run both services:

1. **Backend (awos-core)**
2. **Slack App (slack-app)**

The Slack app communicates with the backend to execute missions and return results.

# 🎯 Project Workflow

```text
User
   │
   ▼
Slack
   │
   ▼
Mission Created
   │
   ▼
Analyzer
   │
   ▼
Classifier
   │
   ▼
Gemini Reasoning
   │
   ▼
Planner
   │
   ▼
LangGraph Workflow
   │
   ▼
AI Agents
   │
   ▼
GitHub MCP
   │
   ▼
QA Validation
   │
   ▼
Slack Response
```

---

# 📊 Current Project Status

- ✅ Project Structure Completed
- ✅ Repository Initialized
- ✅ Core Development Started
- 🔄 Slack Integration In Progress
- 🔄 GitHub MCP Development In Progress
- 🔄 Documentation In Progress
- ⏳ System Integration Pending
- ⏳ Final Testing Pending

---

# 🔮 Future Scope

- Multi-MCP Support
- Autonomous Planning
- Cloud Deployment
- Enterprise Integrations
- Multi-LLM Support
- Advanced Agent Collaboration

---

# 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

# 🙌 Acknowledgements

Developed as part of the **AWOS (Autonomous Workforce Operating System)** project by:

- Johney
- Lokesh
- Manaswitha
- Devaj
