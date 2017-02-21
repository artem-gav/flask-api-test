from flask_restful import Resource
from flask import abort
from Models import Product
from Models.Model import ObjectId, removeNoneElementArray
from Models.Product import validator_put, validator_list_get, validator_list_post, validator_get

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
        if not ObjectId.is_valid(product_id):
            return None

        parser = validator_get()

        args = parser.parse_args()
        return Product.get(product_id, args)

    def delete(self, product_id):
        return Product.remove(product_id)

    def put(self, product_id):
        parser = validator_put()

        args = parser.parse_args()
        args = removeNoneElementArray(args)

        return Product.update(product_id, args)