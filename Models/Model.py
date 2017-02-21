from flask import make_response
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
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

def validator_filters(args):
    if args.filters is not None:
        response.filters = strToJson(args.filters)
    else:
        response.filters = None

    if args.fields is not None:
        response.fields = strToJson(args.fields)
    else:
        response.fields = None

    if args.sort is not None:
        response.sort = strToJson(args.sort)
    else:
        response.sort = [("_id", -1)]

    if args.limit is not None:
        response.limit = int(args.limit)
    else:
        response.limit = 0

    if args.skip is not None:
        response.skip = int(args.skip)
    else:
        response.skip = 0

    return response



def toJson(data):
    return json_util.dumps(data, sort_keys=True, indent=4, default=json_util.default)

def strToJson(data):
    data = data.replace("'", '"')
    return json.loads(data)