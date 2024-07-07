from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm(model, temperature):
    llm = ChatOpenAI(
        model=model,
        temperature=temperature
    )
    return llm