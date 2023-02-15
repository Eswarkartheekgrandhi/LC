from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def getMongoConnection(dbName, collectionName):
    mongoURL = getenv('mongoURL').format(getenv('mongoUsername'),getenv('mongoPassword'))
    print(mongoURL)
    conn = MongoClient(mongoURL)
    db = conn[dbName]
    collection = db[collectionName]
    return conn, collection
