# 👤 User Guide

## Overview

AWOS is an AI-powered autonomous workforce platform that converts user missions into structured execution plans using multiple AI agents.

---

## Current Features

- Mission Creation
- Mission Execution
- Gemini AI Reasoning
- LangGraph Workflow

---

## Upcoming Features

- Slack Integration
- GitHub MCP
- Human-in-the-Loop
- Multi-Agent Collaboration

---

## Running the Backend

Install dependencies

```bash
python -m pip install -r requirements.txt
```

Run FastAPI

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```
---

# Example Mission

Research Cyber Security

Expected Output:

- Analyze Mission
- Generate AI Reasoning
- Create Execution Plan
- Search GitHub Repositories
- Return Relevant Results

Status: Verified ✅