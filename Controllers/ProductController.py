from flask import make_response
from flask_restful import Resource, reqparse
from Models import Product

parser = reqparse.RequestParser()

parser.add_argument('model')
parser.add_argument('quantity')
parser.add_argument('price')

class ProductListControler(Resource):
    def get(self):
        return make_response(Product.getAll(), 200)

    def post(self):
        args = parser.parse_args()
        return Product.add(args), 200

class ProductControler(Resource):
    def get(self, product_id):
        return Product.get(product_id), 200

    def delete(self, product_id):
        return Product.remove(product_id), 204

    def put(self, product_id):
        args = parser.parse_args()
        return Product.update(args, product_id), 204