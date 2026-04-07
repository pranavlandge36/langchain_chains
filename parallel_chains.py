from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model1 = ChatHuggingFace(llm=llm)

model2 = ChatOpenAI(
    model="openai/gpt-oss-120b:free",  # or any model from OpenRouter
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)
prompt1=PromptTemplate(
    template='generate a short summary on: {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template="""
Generate EXACTLY 5 questions and answers based on the text: {text}

Format:
Q1: ...
A1: ...
Q2: ...
A2: ...
...
""",
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='merge provided information and questions and answers in structured format:{summary}and{qna}',
    input_variables=['summary','qna']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'summary': prompt1 | model1 | parser,
    'qna': prompt2 | model2 | parser
})


merge_chain = prompt3 | model1 | parser

chain= parallel_chain | merge_chain
text="""Anthony Edward Stark is a fictional character primarily portrayed by Robert Downey Jr. in the Marvel Cinematic Universe (MCU) media franchise—based on the Marvel Comics character of the same name—commonly known by his alias, Iron Man. Stark is initially depicted as an industrialist, genius inventor, and former playboy who is CEO of Stark Industries. Initially the chief weapons manufacturer for the U.S. military, he has a change of heart and redirects his technical knowledge into creating mechanized suits of armor, which he uses to defend Earth.

Stark becomes a founding member and eventual leader of the Avengers. Following his failed Ultron Program, the internal conflict within the Avengers due to the Sokovia Accords, and Thanos successfully erasing half of all life in the Blip, Stark retires, marries Pepper Potts, and they have a daughter named Morgan. However, Stark rejoins the Avengers on a final mission to undo Thanos' actions. He engineers a time travel device, and the Avengers successfully restore trillions of lives across the universe before Stark ultimately sacrifices his life to defeat Thanos and his army. He chooses Peter Parker as his successor.

Stark is one of the central figures of the MCU, having appeared in nine films as of 2024. The character and Downey's performance have been credited with helping to cement the MCU as a multi-billion-dollar franchise, with Stark's evolution often considered the defining arc of the series. Alternate versions of Stark from within the MCU multiverse appears in various Disney+ animated series, voiced by Mick Wingert."""
result=chain.invoke({'text':text})
print(result)
# chain.get_graph().print_ascii()