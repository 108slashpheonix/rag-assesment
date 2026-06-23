import os
import re
from langchain_community.vectorstores import FAISS

from embedding_selector import get_embeddings
from llm_selector import get_llm

class DoctorCopilot:

    def __init__(self):

        self.embeddings = get_embeddings()

        self.vectorstore = FAISS.load_local(
            "patient_vector_db",
            self.embeddings,
            allow_dangerous_deserialization=True
        )
        docs = self.vectorstore.similarity_search("test",k=3)

        # for doc in docs:
        #     print(doc.metadata)
        self.llm = get_llm()
    
    @staticmethod
    def extract_patient_id(query: str):
        match = re.search(r"PT-\d+", query, re.IGNORECASE)
        if match:
            return match.group(0).upper()
        return None

    def ask(self, query: str):
        patient_id = self.extract_patient_id(query)
        docs = self.vectorstore.similarity_search(
            query,
            k=10,
            filter={"patient_id": patient_id}
        )

        print("\n============================")
        print("TOP 10 RETRIEVED CHUNKS")
        print("============================")

        for i, doc in enumerate(docs, start=1):
            print(f"\n--- Chunk {i} ---")
            print(doc.page_content)
            print(doc.metadata)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
                    You are a clinical AI assistant.
                    User Query:
                    {query}
                    Retrieved Clinical Notes:
                    {context}

                    Instructions:
                    - Use only the retrieved notes.
                    - Summarize relevant findings.
                    - If information is insufficient, say so.
                    - Keep the summary concise.

                    Summary:
                    """
        response = self.llm.invoke(prompt)
        return response.content


if __name__ == "__main__":

    copilot = DoctorCopilot()

    query = input("Enter your query: ")

    answer = copilot.ask(query)

    print("\n============================")
    print("FINAL SUMMARY")
    print("============================\n")

    print(answer)