from pymongo import MongoClient
from flask import make_response
from bson import json_util
from bson.objectid import ObjectId

# init function ObjectId from Model
ObjectId = ObjectId

client = MongoClient()
db = client.api_test_db

def response(response, status=200):
    response = toJson(response)
    response = make_response(response, status)
    response.headers['Content-Type'] = 'application/json'

    return response

def toJson(data):
    return json_util.dumps(data, sort_keys=True, indent=4, default=json_util.default)