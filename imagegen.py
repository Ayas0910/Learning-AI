from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from openai import OpenAI
import base64
from pathlib import Path

load_dotenv()

client = OpenAI()

HERE = Path(__file__).parent

def save(result,filename):
    path = HERE/filename
    path.write_bytes(base64.b64decode(result.data[0].b64_json))

model = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

writer = (ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you write short, visual image prompts. One sentence, no preamble."
        ),
        (
            "human",
            "An illustratio for the blog post about {topic}"
        )
    ]
    ) | model | StrOutputParser()
)

image_prompt = writer.invoke({
    "topic": "learning Langchain"
})

print(image_prompt)
print()
print("-"*50)

result = client.images.generate(
    model = "gpt-image-1-mini",
    prompt = image_prompt,
    size = "1024x1024",
    quality = "low"
)

save(result,"telusko.png")

