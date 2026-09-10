import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage


# Load environment variables from .env
load_dotenv()

# Make the console support UTF-8 characters
sys.stdout.reconfigure(encoding="utf-8")


# --------------------------------------------------
# Tools
# --------------------------------------------------

@tool
def current_time(city: str) -> str:
    """Get the current time in a city."""

    zones = {
        "mumbai": "Asia/Kolkata",
        "london": "Europe/London",
        "new york": "America/New_York",
    }

    zone = zones.get(city.lower())

    if zone is None:
        return f"I do not know the timezone for {city}."

    return datetime.now(
        ZoneInfo(zone)
    ).strftime("%d %B %Y, %I:%M %p")


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the exact result."""

    return a * b


# --------------------------------------------------
# Tool setup
# --------------------------------------------------

# Put our tools into a list
tools = [current_time, multiply]

# Map the tool name to the actual Python tool
tools_by_name = {
    t.name: t
    for t in tools
}


# --------------------------------------------------
# Model setup
# --------------------------------------------------

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
).bind_tools(tools)


# --------------------------------------------------
# Conversation
# --------------------------------------------------

messages = [
    SystemMessage(
        content="You are a helpful assistant. Use the tools when they fit."
    ),
    HumanMessage(
        content="What time is it in Mumbai, and what is 98765 times 43210?"
    ),
]


# --------------------------------------------------
# Agent loop
# --------------------------------------------------

step = 1

while True:

    # Send the conversation to the model
    response = model.invoke(messages)

    # Add the model's response to the conversation
    messages.append(response)

    # If there are no tool calls, we have the final answer
    if not response.tool_calls:
        print("\nFinal answer:")
        print(response.content)
        break

    print(
        f"Step {step}: "
        f"the model asked for {len(response.tool_calls)} tool call(s)"
    )

    # Run every tool requested by the model
    for call in response.tool_calls:

        # Get the actual Python tool using its name
        tool_to_run = tools_by_name[call["name"]]

        # Execute the tool
        tool_message = tool_to_run.invoke(call)

        print(
            f"   {call['name']}({call['args']}) "
            f"<> {tool_message.content}"
        )

        # Add the tool result back into the conversation
        messages.append(tool_message)

    step += 1


# --------------------------------------------------
# Show all message types
# --------------------------------------------------

print(
    "\nMessages in the conversation:",
    [type(m).__name__ for m in messages]
)