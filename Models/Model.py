from pymongo import MongoClient
from flask import jsonify, make_response
from bson import json_util
from bson.objectid import ObjectId

client = MongoClient()
db = client.api_test_db

def toJson(data):
    return jsonify(json_util.dumps(data, sort_keys=True, indent=4, default=json_util.default))