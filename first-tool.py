from langchain_core.tools import tool

from datetime import datetime
from zoneinfo import ZoneInfo


@tool
def current_time(city: str) -> str:
    """Get the current time in the city. useit whenever user ask about time"""
    zones = {
        "mumbai": "Asia/Kolkata",
        "delhi": "Asia/Kolkata",
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
def multiply(a: int,b :int) -> int:
    """Multiply three number and send the exact result"""
    return a * b;

# print(current_time.name)
# print(current_time.description)
# print(current_time.args)

# print(multiply.invoke({
#     "a":5,
#     "b":10
# }))

