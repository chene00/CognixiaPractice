from pydantic import BaseModel
from enum import Enum

# Create an Enum class for Account Type. That way we can specify exactly what type of accounts there are
# Need to inherit from str as well as Enum. Helps FastAPI convert to JSON
class AccountType(str, Enum):
    SAVINGS = "savings"
    CHECKING = "checking"

# Create a class for accounts. Include a customer_id attriute so we know what customer that account belongs to (RELATIONAL)
class Account(BaseModel):
    id : int
    customer_id : int
    type : AccountType
    balance : float

