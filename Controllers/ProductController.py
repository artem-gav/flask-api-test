from flask_restful import Resource
from Models import Product
from Models.Product import validator_put, validator_list_get, validator_list_post, validator_get
from Models.Model import strToJson
import json

class ProductListControler(Resource):
    def get(self):
        parser = validator_list_get()

        args = parser.parse_args()
        return Product.getAll(args)

    def post(self):
        parser = validator_list_post()

        args = parser.parse_args()
        return Product.add(args)

class ProductControler(Resource):
    def get(self, product_id):
        parser = validator_get()

        args = parser.parse_args()

        return Product.get(product_id, args)

    def delete(self, product_id):
        return Product.remove(product_id)

    def put(self, product_id):
        parser = validator_put()

        args = parser.parse_args()
        return Product.update(args, product_id)