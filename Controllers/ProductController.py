from flask_restful import Resource
from Models import Product
from Models.Product import validator

parser = validator()

class ProductListControler(Resource):
    def get(self):
        parser.add_argument('sort')
        parser.add_argument('filters', default=None)
        parser.add_argument('fields', default=None)
        parser.add_argument('limit', default=0)

        args = parser.parse_args()
        return Product.getAll(args)

    def post(self):
        args = parser.parse_args()
        return Product.add(args)

class ProductControler(Resource):
    def get(self, product_id):
        return Product.get(product_id)

    def delete(self, product_id):
        return Product.remove(product_id)

    def put(self, product_id):
        args = parser.parse_args()
        return Product.update(args, product_id)