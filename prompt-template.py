from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you are a {language} trainer. keep answers under {limit} words"
        ),
        (
            "human",
            "Explain {topic} to a begineer."
        )
    ]
)

filled = prompt.invoke(
    {
        "language": "python",
        "limit": 50,
        "topic": "decorators"
    }
)

print(filled.messages)
print()


response = model.invoke(filled)

print(response.content)
