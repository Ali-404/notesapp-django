from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "notes"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
