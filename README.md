agentic-research-assistant/

├── app/
│
├── agents/
│   ├── critic_agent.py
│   ├── llm.py
│   ├── mode_router_agent.py
│   ├── planner_agent.py
│   ├── research_synthesizer_agent.py
│   ├── summarizer_agent.py
│   └── supervisor_agent.py
│
├── graph/
│   ├── agent_state.py
│   ├── nodes.py
│   └── workflow.py
│
├── prompts/
│   ├── critic_prompt.py
│   ├── mode_router_prompt.py
│   ├── planner_prompt.py
│   ├── research_synthesizer_prompt.py
│   ├── summarizer_prompt.py
│   └── supervisor_prompt.py
│
├── rag/
│   ├── document_loader.py
│   ├── embedding_manager.py
│   ├── ingestion_pipeline.py
│   ├── retriever.py
│   └── text_splitter.py
│
├── schemas/
│   └── research_plan.py
│
├── tools/
│   ├── rag_tool.py
│   ├── retrieval_tool.py
│   └── web_search_tool.py
│
├── vectorstore/
│   ├── chroma_manager.py
│   └── vector_store.py
│
├── config.py
│
├── app_ui.py
├── main.py
│
├── chroma_db/
├── data/
├── tests/
│
├── README.md
├── requirements.txt
└── pyproject.toml




# Agentic Research Assistant - Architecture Documentation

## Overview

A LangGraph-powered multi-agent research assistant that combines Retrieval-Augmented Generation (RAG), web search, planning, synthesis, and self-critique to answer both factual and research-oriented queries.

## System Components

### UI Layer

* Streamlit

### Orchestration Layer

* LangGraph
* AgentState
* Workflow

### Agent Layer

* Mode Router Agent
* Supervisor Agent
* Planner Agent
* Summarizer Agent
* Research Synthesizer Agent
* Critic Agent

### Retrieval Layer

* ChromaDB
* Sentence Transformers
* Retriever
* RAG Tool
* Tavily Web Search

### Research Workflow

Mode Router → Planner → Research Tasks → Hybrid Retrieval → Synthesizer → Critic

### QA Workflow

Mode Router → Supervisor → RAG/Web → Summarizer → Critic
