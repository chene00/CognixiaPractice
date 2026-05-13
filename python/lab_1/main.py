from fastapi import FastAPI

# FastAPI uses pydantic to data valdiation and parsing
from pydantic import BaseModel

# Library used to add an optional tag
from typing import Optional

"""
Create User class that extends BaseModel from Pydantic. BaseModel provides several
benefits to User like auto creating __init, casting variable to their specific data type, 
converting data between json strings and dictonaries. 
And documentation for FastAPI to generate the /docs
"""
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

# Create the app by creating a FastAPI object
app = FastAPI()

# Make the auto-incrementing ID
curr_id = 1

# Create an empty in memory database
database = []

"""
GET request at root that returns a string
"""
@app.get("/")
def read_root():
    return {"message": "Hello World"}

"""
POST request that creates a User by having the client provide the user details
"""
@app.post("/users", status_code = 201, response_model=User)
def create_user(user:User):
    global curr_id
    user.id = curr_id
    database.append(user)
    curr_id += 1
    return user

"""
GET request that prints the in memory database
"""
@app.get("/users")
def read_users():
    return database

"""
curl commands:

"""