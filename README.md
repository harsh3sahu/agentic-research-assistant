# Agentic Research Assistant V2

## Overview

Agentic Research Assistant is a production-style GenAI application that combines RAG, multi-step research workflows, corpus-level analysis, report generation, and infographic creation.

The system can:

* Answer questions from uploaded PDFs
* Perform multi-step research workflows
* Generate comprehensive research reports
* Create corpus-level summaries across multiple documents
* Generate infographic blueprints
* Persist knowledge using ChromaDB
* Support human-in-the-loop research decisions

---

## Features

### PDF Upload & Ingestion

* Upload multiple PDFs
* Automatic document ingestion
* Text chunking
* Embedding generation
* ChromaDB storage

### Persistent Knowledge Base

```text
PDFs
 ↓
Chunks
 ↓
Embeddings
 ↓
ChromaDB
```

All data is stored in a persistent vector database and remains available across application restarts.

---

### Retrieval-Augmented Generation (RAG)

```text
Query
 ↓
Semantic Search
 ↓
Relevant Chunks
 ↓
LLM
 ↓
Answer
```

The system retrieves relevant information from uploaded documents before generating responses.

---

### Research Mode

Complex research questions are automatically broken into multiple research tasks and executed across the knowledge base.

Outputs include:

* Research findings
* Consolidated answers
* Confidence scores
* Critique and refinement

---

### Corpus Report Generation

Generate a complete report from all uploaded PDFs without asking a question.

```text
All PDFs
 ↓
Corpus Analysis
 ↓
Research Report
```

Report Sections:

* Executive Summary
* Main Themes
* Key Findings
* Insights
* Recommendations
* Conclusion

---

### Hierarchical Summarization

Large document collections are processed using hierarchical summarization.

```text
Corpus
 ↓
Split into Sections
 ↓
Parallel Summaries
 ↓
Merged Summary
 ↓
Final Report
```

Benefits:

* Lower token consumption
* Faster processing
* Better scalability
* Support for large document collections

---

### Infographic Generation

Generate infographic blueprints from research reports.

Outputs include:

* Title
* Main Theme
* Key Insights
* Key Statistics
* Visual Elements
* Layout Suggestions

---

### Human-in-the-Loop Research

When document retrieval is insufficient, users can decide whether to:

* Continue with existing context
* Expand research using external sources

This provides greater control and transparency over the research process.

---

## Tech Stack

### Backend

* Python 3.11+
* LangChain
* LangGraph

### LLMs

* Groq
* Gemini

### Vector Database

* ChromaDB

### Embeddings

* sentence-transformers/all-MiniLM-L6-v2

### Search

* Tavily

### Frontend

* Streamlit

---

## Project Structure

```text
app/

├── agents/
├── graph/
├── rag/
├── vectorstore/
├── prompts/
├── tools/
└── ui/
```

---


## Highlights

* Agentic AI Architecture
* LangGraph Workflows
* Persistent ChromaDB Storage
* Retrieval-Augmented Generation (RAG)
* Multi-Step Research Planning
* Hierarchical Summarization
* Corpus-Level Intelligence
* Research Report Generation
* Infographic Generation
* Human-in-the-Loop Research
