import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

#change encode into utf-8 format

sys.stdout.reconfigure(encoding='utf-8')

#create out tools

@tool
def multiple(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a*b

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a+b

#put our tools into the list

tools = [multiple,add]

#create the dictionary so llm can easitly lookup and take the tool

tools_by_name = {
    t.name : t for t in tools
}

#bind the tools to the llm

model = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature = 0
).bind_tools(tools)

#create the conversion 

messages = [
    SystemMessage(
        content = "you are the helpful assistant. Use the tools when they fit"
    ),
    HumanMessage(
        content = "add 2 and 3, then multiply the result by 4"
    ),
]

#start the tool calling loop

step = 1

while True:
    response = model.invoke(messages)