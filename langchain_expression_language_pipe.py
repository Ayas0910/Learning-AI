from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful tutor. Answer in {limit} words or less"
        ),
        (
            "user",
            "{questions}"
        )
    ]
)

model = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

text_parse = StrOutputParser()

chain = prompt | model | text_parse

print(chain.invoke({
    "questions": "what is your knowledge cut-off",
    "limit": 5
}))
