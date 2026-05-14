from motor.motor_asyncio import AsyncIOMotorClient
from config.config import settings

db_client: AsyncIOMotorClient = None

def connect_to_mongo():
    global db_client
    db_client = AsyncIOMotorClient(settings.MONGODB_URL)
    print("Sucessfully connected to MongoDB")

def close_mongo():
    global db_client

    if db_client is not None:
        db_client.close()
        print("MongoDB connection closed")

def get_database():
    return db_client[settings.DATABASE_NAME]