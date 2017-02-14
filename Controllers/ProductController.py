from flask_restful import Resource, request
from Models import Product

class ProductListControler(Resource):
    def get(self):
        return Product.getAll(), 200

    def post(self):
        return Product.add(request), 200

class ProductControler(Resource):
    def get(self, product_id):
        return Product.get(product_id), 200

    def delete(self, product_id):
        return Product.remove(product_id), 204

    def update(self, product_id):
        return Product.update(request, product_id), 204