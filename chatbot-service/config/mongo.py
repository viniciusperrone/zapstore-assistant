from pymongo import MongoClient

from config.environments import (
    MONGODB_URI,
    MONGODB_DB_NAME
)


client = MongoClient(MONGODB_URI)
mongo = client[MONGODB_DB_NAME]
