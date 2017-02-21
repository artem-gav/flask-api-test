import Model
from Model import response, ObjectId, strToJson
from flask_restful import request, reqparse

products = Model.db.products

def getAll(args):
    if args.filters is not None:
        filters = strToJson(args.filters)
    else:
        filters = None

    if args.fields is not None:
        fields = strToJson(args.fields)
    else:
        fields = None

    if args.sort is not None:
        sort = strToJson(args.sort)
    else:
        sort = [("_id", -1)]

    if args.limit is not None:
        limit = int(args.limit)
    else:
        limit = 0

    return response(products.find(filters, fields).sort(sort).limit(limit))

def get(product_id):
    return response(products.find_one({'_id': ObjectId(product_id)}))

def add(params):
    result = products.insert(params)
    return response(result)

def update(params, product_id):
    result = products.update(params, {'_id': ObjectId(product_id)})
    return response(result)

def remove(product_id):
    result = products.remove({'_id': ObjectId(product_id)})
    return response(result)

def validator():
    parser = reqparse.RequestParser()

    parser.add_argument('model', location='form')
    parser.add_argument('quantity', type=int, location='form')
    parser.add_argument('price', location='form')

    return parser
