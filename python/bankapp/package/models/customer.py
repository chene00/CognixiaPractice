from pydantic import BaseModel, EmailStr

# Create a customer class. Make sure to import the Account class so we can make an attribute that is a list of objects account
# Initalize to empty just in case the customer hasn't opened an account yet
class Customer(BaseModel):
    id : str
    name : str
    email : EmailStr

class CustomerCreate(BaseModel):
    name : str
    email : EmailStr