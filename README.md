# Doctor Co-Pilot – Metadata-Filtered RAG System

A Retrieval-Augmented Generation (RAG) system that enables doctors to query historical patient records and receive concise AI-generated clinical summaries.

## Overview

This project implements a **Metadata-Filtered RAG Architecture** using:

* FAISS Vector Database
* LangChain
* Local Embedding Models (LM Studio)
* Gemma 4 / OpenAI GPT Models
* Metadata-Based Retrieval

The system allows doctors to ask questions about a specific patient, such as:

```text
Summarize the previous cardiac complications for patient PT-8829
```

The application retrieves the most relevant clinical notes belonging only to the specified patient and uses an LLM to generate a concise summary.

---

## Architecture

```text
Doctor Query
      │
      ▼
Patient ID Extraction
      │
      ▼
Metadata Filter
      │
      ▼
FAISS Similarity Search
      │
      ▼
Top Relevant Clinical Notes
      │
      ▼
Prompt Construction
      │
      ▼
LLM (Gemma 4 / GPT)
      │
      ▼
Clinical Summary
```

### Workflow

1. Doctor submits a natural language query.
2. System extracts the patient ID using deterministic Python logic.
3. Metadata filtering restricts retrieval to records belonging to that patient.
4. Query is embedded using the embedding model.
5. FAISS performs semantic similarity search.
6. Top-K relevant clinical notes are retrieved.
7. Retrieved notes are passed to the LLM.
8. LLM generates a grounded clinical summary.

---

## Why Metadata Filtering?

A standard similarity search across the entire vector database may retrieve semantically similar records belonging to other patients.

To improve:

* Privacy
* Retrieval Accuracy
* Relevance
* Clinical Safety

the system first extracts the patient identifier and applies a metadata filter before semantic retrieval.

Example:

```python
filter={"patient_id": "PT-8829"}
```

This ensures that only records belonging to the requested patient are considered during retrieval.

---

## Why a Hybrid Architecture?

This solution combines deterministic software engineering techniques with LLM-based reasoning.

### Deterministic Logic

* Patient ID extraction
* Metadata filtering
* Retrieval orchestration

### Semantic Retrieval

* Embedding generation
* Vector similarity search using FAISS

### LLM Reasoning

* Clinical summarization
* Natural language generation

This hybrid approach improves relevance, privacy, and factual grounding while reducing hallucinations.

---

## Project Structure

```text
.
├── build_vector_db.py
├── doctor_copilot.py
├── embedding_selector.py
├── llm_selector.py
├── mock_patient_records.jsonl
├── patient_vector_db/
├── .env
└── README.md
```

---

## Components

### build_vector_db.py

Responsible for:

* Loading patient records
* Creating LangChain Documents
* Attaching metadata
* Generating embeddings
* Building the FAISS index

Example metadata:

```json
{
  "patient_id": "PT-8829",
  "doctor_name": "Dr. Suresh",
  "admission_date": "2024-04-24"
}
```

---

### embedding_selector.py

Provides the embedding model used during:

* Index creation
* Query embedding

Default model:

```text
text-embedding-qwen3-embedding-0.6b
```

Running locally through LM Studio.

---

### llm_selector.py

Selects the LLM backend.

Priority:

1. OpenAI GPT models (if OPENAI_API_KEY is configured)
2. Local Gemma 4 via LM Studio

Supported Models:

* GPT-4o
* GPT-4.1
* GPT-5
* Gemma 4

---

### doctor_copilot.py

Main application entry point.

Responsibilities:

* Query processing
* Patient ID extraction
* Metadata-filtered retrieval
* Prompt generation
* Summary generation

---

## To use

### Clone Repository

```bash
git clone <repository-url>
cd doctor-copilot
```

### Create Virtual Environment

mac os / Linux:
```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

If no API key is provided, the application automatically uses LM Studio.

---

## Build Vector Database

```bash
python build_vector_db.py
```

Output:

```text
Vector DB created successfully
```

---

## Run the Application

```bash
python doctor_copilot.py
```
Enter query when
```text
Enter your query:
```
appears in terminal

Example Query:

```text
Summarize the previous cardiac complications for patient PT-8829
```

Example Output:

```text
Patient experienced recurrent cardiac complications including...
```

---

## Technologies Used

* Python
* LangChain
* FAISS
* OpenAI SDK
* LM Studio
* Gemma 4
* GPT Models
* Vector Embeddings
* Retrieval-Augmented Generation (RAG)

---
