import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0.5,
) 

promptTemplate = PromptTemplate.from_template(
  "Say this is a hello world from {name}"
)

prompt = promptTemplate.format(name="vitoriano")

resp = llm.invoke(prompt)

print(resp.content)
