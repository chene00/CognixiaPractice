# The actual fastapi framework
from fastapi import FastAPI, HTTPException

# FastAPI uses pydantic to data valdiation and parsing. Field is used to add requirements
# to the variables declared in a pydantic class
from pydantic import BaseModel, Field

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
    # ... means required field, while min_length makes sure its not empty
    name: str = Field(..., min_length=1)
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
    # Check to make sure that the user you are trying to add doesn't have the same email
    # as someone that is already in the database
    for old_user in database:
        if old_user.email == user.email:
            raise HTTPException(status_code=400, detail="Cannot use a duplicate email")
            
    
    # Add the user by setting their id to an auto-incrementing variable then add to list

    # Must use global to make sure we are using the correct curr_id not the local copy
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
    # Return the list of users
    return database

"""
GET request that finds a user based off their id
"""

@app.get("/users/{id}")
def read_specific_user(id: int):
    # Loop through the list of users until we find the user with the matching id
    for user in database:
        if user.id == id:
            return user

    raise HTTPException(status_code=404, detail="User not found")

"""
PUT request that allows you to modify a user based off their id
"""
@app.put("/users/{id}")
def modify_user_id(id: int, user:User):
    target_user = None

    # Find the target user we are trying to modify
    for db_user in database:
        if db_user.id == id:
            target_user = db_user
            break

    # If we couldn't find him then he doesn't exist
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Loop through to make sure we aren't trying to modify user's email to be the same as 
    # an existing email within in the database that isn't the user itself
    for db_user in database:
        if db_user.email == user.email and db_user.id != id:
            raise HTTPException(status_code=400, detail="Cannot use a duplicate email")

    # Modify the user
    target_user.name = user.name
    target_user.email = user.email

    return user

"""
Delete request that allows you to delete a user based off their id
"""
@app.delete("/users/{id}")
def delete_user(id: int):
    # Loop through the list of users until we find the user we want to remove
    for user in database:
        if user.id == id:
            database.remove(user)
            return

    raise HTTPException(status_code=404, detail="User not found")