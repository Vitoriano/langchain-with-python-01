import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0.5,
) 

prompt = "Say this is a test"

resp =  llm.invoke(prompt)

print(resp.content)
