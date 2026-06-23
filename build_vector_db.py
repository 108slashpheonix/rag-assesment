import json
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from embedding_selector import get_embeddings


def load_documents():

    docs = []

    with open("mock_patient_records.jsonl") as f:

        for line in f:

            row = json.loads(line)

            docs.append(
                            Document(
                                page_content=row["text"],
                                metadata={
                                    "patient_id": row["patient_id"],
                                    "doctor_name": row["doctor_name"],
                                    "admission_date": row["admission_date"]
                                }
                            )
            )

    return docs

def build_vector_db():

    docs = load_documents()

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )
    vectorstore.save_local("patient_vector_db")

    print("Vector DB created successfully")


if __name__ == "__main__":
    build_vector_db()