from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model = "gpt-4o-mini"
)

image_url = "https://tse1.explicit.bing.net/th/id/OIP.3BW94N7eK3qeOX7-EUVGXgHaI4?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"

url_message = HumanMessage(
    content=[
        {
            "type":"text",
            "text": "Describe the message in two sentence"
        },
        {
            "type":"image",
            "url": "image_url"
        }
        
    ]
)
response = model.invoke([url_message])

print(response.content)