from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini")

response = model.invoke("what is the meaning of ayas");

print(response.content)