from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="mistral:latest",temperature = 0)

response = model.invoke("What is your name?")

print(response.content)

chain = (ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a concise assistant"
    ),
    (
        "user",
        "{questions}"
    )
]) | model | StrOutputParser())

for piece in chain.stream({
    "questions": "Why most companies use local ai model"
}):
    print(piece,end="",flush=True)

