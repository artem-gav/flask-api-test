import Model

products = Model.db.products

def getAll():
    return Model.toJson(products.find())

def add(model, quantity, price):
    return products.insert({'model': model, 'quantity': quantity, 'price': price})

def remove(id):
    return products.remove({'_id': Model.ObjectId(id)})