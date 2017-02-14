from pymongo import MongoClient
# import json
from bson import json_util
from bson.objectid import ObjectId

client = MongoClient()
db = client.api_test_db

def toJson(data):
    return json_util.dumps(data, default=json_util.default)