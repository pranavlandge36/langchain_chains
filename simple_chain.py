from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
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

prompt= PromptTemplate(
    template='Give information about {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

chains= prompt | model | parser

result= chains.invoke({'topic': 'top 5 value for money cars based on engine performance'})
print(result)

chains.get_graph().print_ascii()