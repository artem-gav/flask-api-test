import Model
from Model import response, ObjectId, strToJson
from flask_restful import request, reqparse

products = Model.db.products

def getAll(args):

    if args.sort is not None:
        sort = strToJson(args.sort)
    else:
        sort = [("_id", -1)]

    return response(
                products
                    .find(strToJson(args.filters), strToJson(args.fields))
                    .sort(sort)
                    .skip(int(args.skip))
                    .limit(int(args.limit))
            )

def get(product_id, args):
    return response(products.find_one({'_id': ObjectId(product_id)}, strToJson(args.fields)))

def add(params):
    result = products.insert(params)
    return response(result)

def update(params, product_id):
    result = products.update(params, {'_id': ObjectId(product_id)})
    return response(result)

def remove(product_id):
    result = products.remove({'_id': ObjectId(product_id)})
    return response(result)

# Validators for request params
def validator_list_get():
    parser = reqparse.RequestParser()

    parser.add_argument('sort', default=None, type=str)
    parser.add_argument('filters', default=None, type=str)
    parser.add_argument('fields', default=None, type=str)
    parser.add_argument('limit', default=0, type=int)
    parser.add_argument('skip', default=0, type=int)

    return parser

def validator_list_post():
    parser = reqparse.RequestParser()

    parser.add_argument('model', type=str, required=True, location='form')
    parser.add_argument('quantity', type=int, required=True, location='form')
    parser.add_argument('price', type=float, required=True, location='form')

    return parser

def validator_put():
    parser = reqparse.RequestParser()

    parser.add_argument('model', type=str, location='form')
    parser.add_argument('quantity', type=int, location='form')
    parser.add_argument('price', type=float, location='form')

    return parser

def validator_get():
    parser = reqparse.RequestParser()

    parser.add_argument('fields', default=None, type=str)

    return parser