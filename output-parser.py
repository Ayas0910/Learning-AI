from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import (StrOutputParser, JsonOutputParser)
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

text_parse = StrOutputParser()

response = model.invoke("Name three python courses for beginners.")

print()

print(text_parse.invoke(response.content))

print()

json_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Reply with json only using the keys name, creator, and year"
        ),
        (
            "human",
            "Tell me about the {topic} framework"
        )
    ]
)

filled = json_prompt.invoke(
    {
        "topic": "java"
    }
)

response = model.invoke(filled)

print()

data = JsonOutputParser().invoke(response)

print(type(data))

print(data["name"],"was created in",data["year"])