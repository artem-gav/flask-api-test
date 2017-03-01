import Model
from Model import response, ObjectId, strToList, is_valid
from flask_restful import reqparse, abort
import logging

fields = {
    'code': {'type': str},
    'description': {'type': str, 'help': 'description'},
    'name': {'type': str, 'help': 'name'},
    'price': {'type': float, 'help': 'price'},
    'source_id': {'type': int, 'help': 'source_id'},
    'variant': {'type': int, 'help': 'variant'},
    'vat': {'type': int, 'help': 'vat'},
    'params': {'type': dict, 'help': 'params'},
    'colour': {'type': str, 'help': 'colour', 'location': 'params'},
    'size': {'type': str, 'help': 'size', 'location': 'params'}
}

validators = {
    'sort': {'default': None, 'type': str},
    'filters': {'default': None, 'type': unicode},
    'fields': {'default': None, 'type': str},
    'limit': {'default': 0, 'type': int},
    'skip': {'default': 0, 'type': int}
}

products = Model.db.products
parser = reqparse.RequestParser()

def getAll(args):
    sort = strToList(args.sort) if args.sort is not None else [("_id", -1)]

    return response(
                products
                    .find(strToList(args.filters), strToList(args.fields))
                    .sort(sort.items())
                    .skip(int(args.skip))
                    .limit(int(args.limit))
            )

def get(product_id, args):
    result = products.find_one({'_id': ObjectId(product_id)}, strToList(args.fields))
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
    for (title, params) in validators.items():
        parser.add_argument(title, default=params['default'], type=params['type'])

    return parser

def validator_list_post():
    for (title, params) in fields.items():
        required = params['required'] if 'required' in params else True
        help = params['help'] if 'help' in params else None

        if 'location' not in params:
            parser.add_argument(title, type=params['type'], required=required, help=help, location=['form', 'json'])
        else:
            # parameters `params` variable
            params_parser = reqparse.RequestParser()
            params_parser.add_argument(title, type=params['type'], required=required, help=help, location=params['location'])

    return parser

def validator_put():
    for (title, params) in fields.items():
        help = params['help'] if 'help' in params else None

        if 'location' not in params:
            parser.add_argument(title, type=params['type'], help=help, location=['form', 'json'])
        else:
            # parameters `params` variable
            params_parser = reqparse.RequestParser()
            params_parser.add_argument(title, type=params['type'], help=help, location=params['location'])

    return parser

def validator_get():
    parser.add_argument('fields', default=None, type=str)

    return parser