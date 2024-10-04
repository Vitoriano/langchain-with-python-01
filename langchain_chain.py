import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain_core.output_parsers import StrOutputParser
from langchain.globals import set_debug


load_dotenv()
set_debug(True)

llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  temperature=0.5,
  api_key=os.getenv("OPENAI_API_KEY")
)

movie_template = ChatPromptTemplate.from_template (
 "Suggest 3 movie titles that have a similar genre to {title} Movies"
)

series_template = ChatPromptTemplate.from_template (
  "Suggest 2 series titles that have a similar genre to {title} Movies"
)

#movieChain = LLMChain(llm=llm, prompt=movie_template)

#serieChain = LLMChain(llm=llm, prompt=series_template)

#chain = SimpleSequentialChain(chains=[movieChain, serieChain])
chain = movie_template | llm | StrOutputParser()


result = chain.invoke("Harry Potter")

print(result)