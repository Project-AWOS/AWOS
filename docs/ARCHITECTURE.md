# 🏗️ AWOS System Architecture

## Overview

The **Autonomous Workforce Operating System (AWOS)** is a multi-agent AI platform that transforms Slack into an AI-powered collaborative workplace.

The system uses **FastAPI**, **LangGraph**, **Google Gemini**, and **Model Context Protocol (MCP)** to coordinate specialized AI agents that analyze, reason, plan, and execute user missions.

---

# High-Level Architecture

```text
                    User
                      │
                      ▼
              Slack Workspace
                      │
                      ▼
              Slack Application
                 (In Progress)
                      │
                      ▼
                 Mission API
                  (FastAPI)
                      │
                      ▼
             Execution Service
                      │
                      ▼
                LangGraph Engine
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
  Analyzer       Classifier      Reasoner
                                        │
                                        ▼
                                  Google Gemini
                                        │
                                        ▼
                                    Planner
                                        │
                                        ▼
                                  Mission Plan
                                        │
                                        ▼
                             GitHub MCP Server
                                (In Progress)
                                        │
                                        ▼
                                   GitHub API
                                        │
                                        ▼
                                Final Response
```

---

# Core Components

## Mission API

Handles:

- Mission Creation
- Mission Retrieval
- Mission Deletion
- Mission Execution

---

## Execution Service

Responsible for coordinating the complete mission execution workflow using LangGraph.

---

## Analyzer

Processes incoming missions by:

- Normalizing text
- Extracting keywords
- Counting words
- Counting sentences

Produces:

**MissionAnalysis**

---

## Classifier

Classifies missions based on:

- Domain
- Category
- Complexity

Produces:

**MissionClassification**

---

## Reasoner

Uses Google Gemini AI to understand the mission and generate structured reasoning.

Produces:

**MissionReasoning**

---

## Planner

Converts reasoning into an executable mission plan containing:

- Summary
- Execution Steps
- Agent Order
- Required Tools

Produces:

**MissionPlan**

---

## LangGraph

LangGraph orchestrates the execution flow.

Current Workflow

START

↓

Analyzer

↓

Classifier

↓

Reasoner

↓

Planner

↓

END

---

# Human-in-the-Loop

The project is designed to support Human-in-the-Loop (HITL), allowing user approval before critical execution stages.

---

# Multi-Agent Architecture

The system is designed around multiple AI agents such as:

- CEO Agent
- Research Agent
- Engineer Agent
- QA Agent

These agents collaborate to complete complex missions.

---

# Current Project Status

| Module | Status |
|----------|--------|
| Repository Setup | ✅ Completed |
| FastAPI Backend | ✅ Completed |
| Analyzer | ✅ Completed |
| Classifier | ✅ Completed |
| Gemini Integration | ✅ Completed |
| Reasoner | ✅ Completed |
| Planner | ✅ Completed |
| LangGraph Workflow | ✅ Completed |
| Mission CRUD APIs | ✅ Completed |
| Swagger Testing | ✅ Completed |
| GitHub MCP | 🔄 In Progress |
| Slack Integration | 🔄 In Progress |
| End-to-End Integration | 🔄 In Progress |