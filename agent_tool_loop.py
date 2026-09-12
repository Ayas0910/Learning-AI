import sys
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

#load the secret key

load_dotenv()

#proper encoding

sys.stdout.reconfigure(encoding="utf-8")

#creating tools

@tool
def multiple(a: int, b: int) ->int:
    """multiple two number"""
    return a*b

@tool
def add(a:int, b:int) -> int:
    """add two number"""
    return a+b

#creating agent

agent = create_agent(
    model = "openai:gpt-4o-mini",
    tools=[multiple,add],
    system_prompt = (
        "You are a helpful assistant"
        "use the tool when they are fit"
    )

)

#invoke the agent

result = agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":(
                    "can you multiply the 4*3 and add the result to the 5"
                )
            }
        ]
    }
)

#print the result

print("final answer:")
print(result["messages"][-1].content)
print()