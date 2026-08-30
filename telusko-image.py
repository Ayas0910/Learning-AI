from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pathlib import Path
import base64



load_dotenv()

model = ChatOpenAI(model = "gpt-4o-mini")

# image_url = "https://th.bing.com/th/id/OIP.g0-gxGa3w9D9SJs5A6Yo_wHaLH?w=120&h=180&c=7&r=0&o=7&dpr=1.4&pid=1.7&rm=3"


# url_message = HumanMessage(
#     content = [
#         {
#             "type": "text",
#             "text": "Describe the image in two sentences."
#         },
#         {
#             "type": "image",
#             "url": image_url
#         }
#     ]
# )

# response = model.invoke([url_message])

# print(response.content)

image_path = Path(__file__).parent/"sample.jpg"

encoded = base64.b64encode(
    image_path.read_bytes()
).decode("utf-8")

url_message = HumanMessage(
    content = [
        {
            "type": "text",
            "text": "Describe the image in two sentences."
        },
        {
            "type": "image",
            "base64": encoded,
            "mime_type": "image/jpeg"
        }
    ]
)

response = model.invoke([url_message])

print(response.content)