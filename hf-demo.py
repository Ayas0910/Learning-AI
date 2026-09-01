from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text generation",
    max_new_tokens = 200,
    temperature = 0.3,
)

model = ChatHuggingFace(llm = endpoint)

response = model.invoke("what is your model name in two lines")

print(response.content)

# I need to study the next class