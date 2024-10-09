import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain_core.output_parsers import StrOutputParser
from langchain.globals import set_debug

from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
#set_debug(True)


class Movie(BaseModel):
  title: str = Field("Need For Speed")


llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  temperature=0.5,
  api_key=os.getenv("OPENAI_API_KEY")
)

parser = JsonOutputParser(pydantic_object=Movie)

movie_template = PromptTemplate (
 template="""Suggest 3 movie titles that have a similar genre to {title} Movies
 {output_format}
 """,
 input_variables=["title"],
 partial_variables={"output_format": parser.get_format_instructions()}
)

chain = movie_template | llm | StrOutputParser()


result = chain.invoke("Fast and Furious")

print(result)