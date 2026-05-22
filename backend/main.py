from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from controllers import account_controller, customer_controller, auth_controller
from db.mongodb import connect_to_mongo, close_mongo
from mangum import Mangum

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()

    yield

    close_mongo()

# Create the actual fastapi app
app = FastAPI(title="Bank App", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Your Vite frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include/link the specific account/customer routers
app.include_router(account_controller.router, prefix="/api")
app.include_router(customer_controller.router, prefix="/api")
app.include_router(auth_controller.router)

# Default message when you navigate to the root
@app.get("/")
def health():
    return {"message" : "Server is up"}

handler = Mangum(app, lifespan="on")