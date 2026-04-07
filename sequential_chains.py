from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='give information about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="""
From the following list of cars:

{data}

Filter top 5 based on engine specs.
""",
    input_variables=["data"]
)


parser=StrOutputParser()

chain = prompt1|model|parser|prompt2|model|parser
result=chain.invoke({'topic':'best cars under 20000000 rs'})
print(result)
chain.get_graph().print_ascii()