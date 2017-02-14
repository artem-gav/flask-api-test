from flask import Flask, request, render_template
from Controllers.MainController import MainControler
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(MainControler, '/<int:product_id>', endpoint="0")

if(__name__ == '__main__'):
    app.run(debug=True)