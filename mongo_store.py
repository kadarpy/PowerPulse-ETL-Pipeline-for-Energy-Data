import pymongo

from config import MONGO_URI
from decorators import log_step

class MongoStore:
    @log_step
    def save(self, data):
        client = pymongo.MongoClient(MONGO_URI)
        db = client["powerpulse"]
        db["raw_data"].insert_one(data)