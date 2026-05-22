from motor.motor_asyncio import AsyncIOMotorClient
from config.config import settings

db_client: AsyncIOMotorClient = None

async def connect_to_mongo():
    global db_client
    try:

        db_client = AsyncIOMotorClient(settings.MONGODB_URL)

        await db_client.admin.command('ping')
        print("Sucessfully connected to MongoDB")
    except Exception as e:
        print("Failed to connect to MongoDB")
        raise e

def close_mongo():
    global db_client

    if db_client is not None:
        db_client.close()
        print("MongoDB connection closed")

def get_database():
    return db_client[settings.DATABASE_NAME]