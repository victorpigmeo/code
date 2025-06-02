from pymongo import MongoClient

CONNECTION_STRING = "mongodb://root:example@localhost:27017/keystroke-detector?authSource=admin"

client = MongoClient(CONNECTION_STRING)
db = client['keystroke-detector']

def get_collection(collection_name):
    return db[collection_name].find()