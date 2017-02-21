from flask import make_response
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId, InvalidId
import json

# init function ObjectId from Model
ObjectId = ObjectId

client = MongoClient()
db = client.api_test_db

def response(response, status=200, headers={'Content-Type': 'application/json'}):
    response = toJson(response)
    response = make_response(response, status)
    response.headers.extend(headers)

    return response

def toJson(data):
    return json_util.dumps(data, sort_keys=True, indent=4, default=json_util.default)

def strToJson(data):
    if data is None:
        return None

    data = data.replace("'", '"')
    return json.loads(data)

def removeNoneElementArray(data):
    for x in list(data.keys()):
        if data[x] == None:
            del data[x]

    return data

@classmethod
def is_valid(cls, oid):
    try:
        ObjectId(oid)
        return True
    except (InvalidId, TypeError):
        return False