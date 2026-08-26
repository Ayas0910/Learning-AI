from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini")

messages = [
    SystemMessage(
        content = "Right now you are python trainer. if some one ask anything about python then say in three bullet points other then they ask you politely say only ask python related query"
    ),
    HumanMessage(
        content = "What is python?"
    )
]

response = model.invoke(messages)

print(response.content)

print(response.usage_metadata)

print(response.response_metadata.get("model_name"))

# messages.append(response)

messages.append(
    HumanMessage(
        content = "what is the first thing I should build"
    )
)

response = model.invoke(messages)

print("------------------------------------------------------")

print(response.content)

print(response.usage_metadata)

print("------------------------------------------------------")


