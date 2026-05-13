from fastapi import FastAPI
from controllers import account_controller, customer_controller

# Create the actual fastapi app
app = FastAPI(title="Bank App")

# Include/link the specific account/customer routers
app.include_router(account_controller.router, prefix="/api")
app.include_router(customer_controller.router, prefix="/api")

# Default message when you navigate to the root
@app.get("/")
def health():
    return {"message" : "Server is up"}