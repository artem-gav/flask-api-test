from flask_restful import Resource
from Models import Product

@api.route()
class MainControler(Resource):
    def get(self):
        return Product.getAll(), 200

    def delete(self, product_id):
        return Product.remove(product_id), 204