from fastapi import FastAPI
from contextlib import asynccontextmanager
from controllers import account_controller, customer_controller
# from db.database import connect_to_mongo, close_mongo

# @asynccontextmanager
# async def lifespan(app: FasAPI):
#     connect_to_mongo()

#     yield

#     close_mongo()

# Create the actual fastapi app
app = FastAPI(title="Bank App")

# Include/link the specific account/customer routers
app.include_router(account_controller.router, prefix="/api")
app.include_router(customer_controller.router, prefix="/api")

# Default message when you navigate to the root
@app.get("/")
def health():
    return {"message" : "Server is up"}