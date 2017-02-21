import Model
from Model import response, ObjectId, strToJson
from flask_restful import request, reqparse

products = Model.db.products

def getAll(args):
    validator_filters = Model.validator_filters(args)

    return response(
                products
                    .find(validator_filters.filters, validator_filters.fields)
                    .sort(validator_filters.sort)
                    .skip(validator_filters.skip)
                    .limit(validator_filters.limit)
            )

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
