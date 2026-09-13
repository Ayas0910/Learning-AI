#Needed package I import here
import sys
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

#load the secret key
load_dotenv()

#encode properly
sys.stdout.reconfigure(encoding="utf-8")

#create the addition tool here
@tool
def add_the_number(a: int, b: int) -> int:
    """"Add the two number"""
    return a+b


#create the agent
agent = create_agent(
    model = "openai:gpt-4o-mini",
    tools= [add_the_number],
    system_prompt = "You are the helpful assistant, give answer in the one line understood and answer politely",
    checkpointer = InMemorySaver()
)

#okay create the helper function with agent invoke there
def ask(question,thread_id):
    response = agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content": question
                }
            ]
        },
        config={
            "configurable":{
                "thread_id":thread_id
            }
        }
    )
    print(f"[{thread_id}] Q:{question}")
    print(f"[{thread_id}] A: {response['messages'][-1].content}")
    print("-"*100)


ask("hello my name is ayas can you able to add 2+2",thread_id="ayas")
ask("What is my name?",thread_id="ayas")
