from pydantic import BaseModel, EmailStr

# Create a customer class. Make sure to import the Account class so we can make an attribute that is a list of objects account
# Initalize to empty just in case the customer hasn't opened an account yet
class CustomerResponse(BaseModel):
    id : str
    name : str
    email : EmailStr

class CustomerCreate(BaseModel):
    name : str
    email : EmailStr
    password : str

class Customer(BaseModel):
    id : str | None = None
    name : str
    email : EmailStr
    hashed_password : str