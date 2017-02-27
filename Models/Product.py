import Model
from Model import response, ObjectId, strToJson, strToList, is_valid
from flask_restful import reqparse, abort

products = Model.db.products
parser = reqparse.RequestParser()

def getAll(args):

    if args.sort is not None:
        sort = strToList(args.sort)
    else:
        sort = [("_id", -1)]

    return response(
                products
                    .find(strToJson(args.filters), strToJson(args.fields))
                    .sort(sort)
                    .skip(int(args.skip))
                    .limit(int(args.limit))
            )

def get(product_id, args):
    result = products.find_one({'_id': ObjectId(product_id)}, strToJson(args.fields))
    return response(result)

def add(params):
    result = products.insert(params)
    return response(result)

def update(product_id, params):
    result = products.update({'_id': ObjectId(product_id)}, {"$set": params})
    return response(result)

def remove(product_id):
    result = products.remove({'_id': ObjectId(product_id)})
    return response(result)

# Validators for request params
def validator_list_get():
    parser.add_argument('sort', default=None, type=str)
    parser.add_argument('filters', default=None, type=str)
    parser.add_argument('fields', default=None, type=str)
    parser.add_argument('limit', default=0, type=int)
    parser.add_argument('skip', default=0, type=int)

    return parser

def validator_list_post():
    parser.add_argument('code', type=str, required=True, location='form')
    parser.add_argument('description', type=str, required=True, location='form')
    parser.add_argument('name', type=str, required=True, location='form')
    parser.add_argument('price', type=float, required=True, location='form')
    parser.add_argument('source_id', type=int, required=True, location='form')
    parser.add_argument('variant', type=int, required=True, location='form')
    parser.add_argument('vat', type=int, required=True, location='form')

    # parser.add_argument('params_colour', type=str, location='form')
    # parser.add_argument('params_size', type=str, location='form')

    return parser

def validator_put():
    parser.add_argument('code', type=str, location='form')
    parser.add_argument('description', type=str, location='form')
    parser.add_argument('name', type=str, location='form')
    parser.add_argument('price', type=float, location='form')
    parser.add_argument('source_id', type=int, location='form')
    parser.add_argument('variant', type=int, location='form')
    parser.add_argument('vat', type=int, location='form')

    # parser.add_argument('params_colour', type=str, location='form')
    # parser.add_argument('params_size', type=str, location='form')

    return parser

def validator_get():
    parser.add_argument('fields', default=None, type=str)

    return parser