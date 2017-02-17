import Model
from Model import response, ObjectId
from flask_restful import request, reqparse

products = Model.db.products

def getAll():
    where = request.args['where']
    return where
    return response(products.find())

def get(product_id):
    return response(products.find_one({'_id': ObjectId(product_id)}))

def add(params):
    return products.insert(params)

def update(params, product_id):
    return products.update(params, {'_id': ObjectId(product_id)})

def remove(product_id):
    return products.remove({'_id': ObjectId(product_id)})

def validator():
    parser = reqparse.RequestParser()

    parser.add_argument('model', location='args')
    parser.add_argument('quantity', type=int, location='args')
    parser.add_argument('price', location='args')

    # parser.add_argument('where', location='json')

    return parser
