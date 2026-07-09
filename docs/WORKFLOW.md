# 🔄 AWOS Workflow

## Overview

AWOS executes user requests through a structured multi-stage workflow powered by FastAPI, LangGraph, and Google Gemini.

---

# Current Workflow

```text
User

↓

Mission API

↓

Execution Service

↓

LangGraph

↓

Analyzer

↓

Classifier

↓

Reasoner (Gemini)

↓

Planner

↓

Mission Plan

↓

JSON Response
```

---

# Workflow Stages

## 1. Mission Creation

The user submits a mission request.

Example:

> Build an AI-powered healthcare application.

---

## 2. Mission API

The FastAPI backend creates and stores a new mission.

---

## 3. Execution Service

The execution service starts the LangGraph workflow.

---

## 4. Analyzer

Analyzes and normalizes the mission.

Outputs:

MissionAnalysis

---

## 5. Classifier

Determines:

- Domain
- Category
- Complexity

Outputs:

MissionClassification

---

## 6. Reasoner

Uses Google Gemini AI to understand the mission and generate structured reasoning.

Outputs:

MissionReasoning

---

## 7. Planner

Creates an execution plan containing:

- Summary
- Steps
- Agent Order
- Required Tools

Outputs:

MissionPlan

---

## 8. Response

Returns the generated mission plan as a JSON response.

---

# Future Workflow

The final workflow will include:

```text
User

↓

Slack Workspace

↓

Mission API

↓

Execution Service

↓

LangGraph

↓

Analyzer

↓

Classifier

↓

Reasoner

↓

Planner

↓

GitHub MCP

↓

Human Approval

↓

Multi-Agent Execution

↓

Slack Response
```

---

# Current Development Stage

- ✅ Mission API
- ✅ Analyzer
- ✅ Classifier
- ✅ Gemini Integration
- ✅ Reasoner
- ✅ Planner
- ✅ LangGraph
- 🔄 GitHub MCP Integration
- 🔄 Slack Integration
- ⏳ Human-in-the-Loop
- ⏳ Multi-Agent Collaboration