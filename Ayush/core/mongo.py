from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import config

from ..logging import LOGGER

# Check Mongo URI
if not config.MONGO_DB_URI:
    LOGGER(__name__).warning("No MONGO DB URL found ❌")
    raise Exception("MongoDB URI is missing! Add MONGO_DB_URI in .env")

# Async Mongo (Motor)
mongo_async_client = AsyncIOMotorClient(config.MONGO_DB_URI)

# Sync Mongo (Pymongo)
mongo_sync_client = MongoClient(config.MONGO_DB_URI)

# Database name (simple & fixed)
mongodb = mongo_async_client["Ayush"]
pymongodb = mongo_sync_client["Ayush"]
