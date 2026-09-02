from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

#streaming directly from model

for chunk in model.stream("Writing the 4 line poem about debugging at midnight"):
    print(chunk.content,end="",flush=True)

chain = ( ChatPromptTemplate.from_messages(
    [
        (
            "human",
            "how {Topic} works"
        )
    ]
) | model | StrOutputParser() )

for piece in chain.stream({"Topic":"the http"}):
    print(piece,end="",flush=True)

