import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv


class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key = os.getenv("GROQ_API_KEY"),  model="llama-3.1-70b-versatile", )

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))