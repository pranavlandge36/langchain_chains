from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import BaseModel, Field 
from typing import Literal
load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     task="text-generation",
#     # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model = ChatHuggingFace(llm=llm)

model = ChatOpenAI(
    model="openai/gpt-oss-120b:free",  # or any model from OpenRouter
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

text=input('write a review \n')

class sentiment(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='sentiment of given text')

parser=StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=sentiment)

prompt1=PromptTemplate(
    template="""
Classify sentiment as positive or negative.

Return ONLY valid JSON.
Do NOT explain.
Do NOT write code.

{text}

{format_instructions}
""",
    input_variables={'text'},
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)
classifier_chain= prompt1 | model | parser2



prompt2=PromptTemplate(
    template='give a appropriate feedback to this positive review to respond to customer . write in short: \n {text}',
    input_variables={'text'}
)

prompt3=PromptTemplate(
    template='write appropriate feedback to this negative review, to respond to customer . write in short: \n {text}',
    input_variables={'text'}
)

branch_chain= RunnableBranch(
    (lambda x: x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser ),
    RunnableLambda(lambda x:'could not find sentiment in review')
)

chain = classifier_chain | branch_chain
result = chain.invoke({'text':text})
print(result)