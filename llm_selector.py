import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():

    openai_key = os.getenv("OPENAI_API_KEY")

    if openai_key:
        print("Using OpenAI")

        return ChatOpenAI(
            model="gpt-4o",
            temperature=0
        )

    return ChatOpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio",
        model="google/gemma-4-e4b",
        temperature=0
    )