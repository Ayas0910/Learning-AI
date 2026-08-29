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
            "you are a {language} trainer. keep answer under the {limit} words"

        ),
        (
            "human",
            "Explain {topic} as a beginner"
        )
    ]
)

prompt.invoke({
    "language" : "python",
        "limit" : 90,
        "topic" : "variables"
}
)
