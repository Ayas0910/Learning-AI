from typing import Literal

from pydantic import BaseModel, Field
from langchain_core.tools import tool


class ConvertInput(BaseModel):
    """Input for the currency converter."""

    amount: float = Field(
        description="How many rupees to convert",
        gt=0
    )

    currency: Literal["USD", "EUR", "GBP"] = Field(
        description="Currency to convert into"
    )


@tool("convert_from_rupees", args_schema=ConvertInput)
def convert_from_rupees(amount: float, currency: str) -> str:
    """Convert an amount in Indian rupees into another currency."""

    rates = {
        "USD": 0.012,
        "EUR": 0.011,
        "GBP": 0.0094
    }

    return (
        f"{amount} rupees is about "
        f"{amount * rates[currency]:.2f} {currency}"
    )


print("args:", convert_from_rupees.args)

print(
    convert_from_rupees.invoke({
        "amount": 5000,
        "currency": "USD"
    })
)