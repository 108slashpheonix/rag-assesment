# Architecture of the RAG Solution

This solution follows a **Metadata-Filtered Retrieval-Augmented Generation (RAG)** architecture.

1. Historical patient clinical notes are converted into vector embeddings and indexed in a FAISS vector database along with associated metadata such as `patient_id`, `doctor_name`, and `admission_date`. 
I used FAISS as its a lightweight local vector store fit for this assessment, although the same architecture can be implemented using managed vector databases such as Pinecone or Weaviate.

2. At query time, the system first extracts the patient identifier from the doctor's natural language query using deterministic Python logic (regex).

3. The extracted patient ID is used as a metadata filter during retrieval, ensuring that only records belonging to the specified patient are considered for semantic search.

4. The query is embedded and a similarity search is performed within the filtered patient records to retrieve the most relevant clinical note chunks.

5. The retrieved notes are combined into a context window and provided to a Large Language Model (LLM). In this implementation, Gemma 4 is executed locally through LM Studio. Alternatively, an OpenAI API key can be configured to use GPT-4o, GPT-4.1, or GPT-5 models.

6. The LLM generates a concise clinical summary grounded exclusively in the retrieved patient records.

This architecture improves retrieval relevance, protects patient privacy by restricting retrieval to a specific patient's records, and reduces hallucinations by grounding responses in historical clinical documentation.

# Why a Hybrid Approach?

I have used hybrid architecture because patient identification is handled through deterministic Python logic, while clinical summarization is handled by the LLM. Retrieval is grounded through vector search, reducing hallucinations and ensuring responses are based on historical patient records.

