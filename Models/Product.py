import Model

products = Model.db.products

def getAll():
    return Model.toJson(products.find())

def get(product_id):
    return Model.toJson(products.find({'_id': Model.ObjectId(product_id)}))

def add(params):
    return products.insert(params)

def update(params, product_id):
    return products.update(params, {'_id': Model.ObjectId(product_id)})

def remove(id):
    return products.remove({'_id': Model.ObjectId(id)})