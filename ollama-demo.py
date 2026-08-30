from langchain_ollama import ChatOllama

model = ChatOllama(model="mistral:latest",temperature = 0)

response = model.invoke("What is your name?")

print(response.content)