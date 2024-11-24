from pymongo import MongoClient

# never expose the connection string in the code
client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.2cpnc.mongodb.net/ytmanager")

db = client["ytmanagaer"]