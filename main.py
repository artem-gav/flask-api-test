from flask import Flask, request, render_template
from Controllers.ProductController import ProductControler, ProductListControler
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(ProductListControler, '/', endpoint="products")
api.add_resource(ProductControler, '/<int:product_id>', endpoint="product")

if(__name__ == '__main__'):
    app.run(debug=True)