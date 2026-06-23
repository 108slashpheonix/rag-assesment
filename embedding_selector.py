from openai import OpenAI
from langchain_core.embeddings import Embeddings

class TextEmbeddings(Embeddings):

    def __init__(self):
        self.client = OpenAI(
            base_url="http://127.0.0.1:1234/v1",
            api_key="lm-studio"
        )
        self.model = "text-embedding-qwen3-embedding-0.6b"

    def embed_documents(self, texts):
        embeddings = []
        
        for text in texts:
            response = self.client.embeddings.create(model=self.model,input=text)
            embeddings.append(response.data[0].embedding)
        return embeddings

    def embed_query(self, text):
        response = self.client.embeddings.create(model=self.model,input=text)
        return response.data[0].embedding

def get_embeddings():
    return TextEmbeddings()