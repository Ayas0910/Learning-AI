from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model = "gpt-4o-mini"
)

print(model.invoke("what is the multiplication of 45678*45678").content)

print("what is the multiplication of 45678*45678",45678*45678)