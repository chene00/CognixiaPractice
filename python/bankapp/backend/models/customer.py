from pydantic import BaseModel, EmailStr
from models.account import Account

# Create a customer class. Make sure to import the Account class so we can make an attribute that is a list of objects account
# Initalize to empty just in case the customer hasn't opened an account yet
class Customer(BaseModel):
    id : int
    name : str
    accounts : list[Account] = []
    email : EmailStr