from flask import Flask
from flask_restful import Api
from Controllers.ProductController import ProductControler, ProductListControler

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(ProductListControler, '/', endpoint="products")
api.add_resource(ProductControler, '/<product_id>', endpoint="product")

if(__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')