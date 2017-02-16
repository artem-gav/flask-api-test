import Model
from Model import response, ObjectId
from flask_restful import reqparse

products = Model.db.products

def getAll():
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

    parser.add_argument('model')
    parser.add_argument('quantity')
    parser.add_argument('price')

    return parser
