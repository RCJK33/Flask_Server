from flask import Flask, request, abort
import json

from config import db
from bson import ObjectId

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/')
def home():
    return "Hello, this is a home page"


@app.get('/api/about')
def about():
    me = {'name:': 'Rafael'}
    return json.dumps(me)

@app.get('/api/version')
def version():
    version = {
        'name': 'apiFLASK!1',
        'version': 35,
        'build': 2948
    }
    return json.dumps(version)

""" @app.get('/test')
def test():
    return '<a href="/about ">about<a/>\n<a href="/api/version ">version<a/>' """

#############################
# API endpoints
# JSON
#############################

def fix_id(obj):
    obj['_id'] = str(obj['_id'])
    return obj

@app.get('/api/products')
def get_products():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

@app.post('/api/products')
def save_product():
    product = request.get_json() # This ias the object that send by client

    if 'name' not in product or len(product['name']) < 3:
        return abort(400, 'Invalid name')
    
    if 'category' not in product or len(product['category']) < 1:
        return abort(400, 'Category is empty')
    
    if 'img' not in product or len(product['img']) < 1:
        return abort(400, 'Image is empty')
    
    if 'price' not in product:
        return abort(400, 'Price is required')
    
    if not isinstance(product['price'],(int,float)):
        return abort(400, 'Price should be a number')

    db.products.insert_one(product)
    return json.dumps(fix_id(product))

@app.get('/api/report/total')
def total():
    dict = {'total': 0, 'count_products':0}
    
    cursor = db.products.find({})
    for prod in cursor:
        dict['total'] += prod['price']
        dict['count_products'] += 1
    return json.dumps(dict)

@app.get('/api/categories')
def categories():
    categories = set()

    cursor = db.products.find({})
    for prod in cursor:
        categories.add(str(prod['category']))
    categories = list(categories)
    categories.sort()
    return json.dumps(categories)

@app.get('/api/products/category/<category>')
def get_products_by_category(category):
    products = []
    cursor = db.products.find({'category':str(category)})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

@app.get('/api/products/search/<text>')
def search_products(text):
    products = []
    cursor = db.products.find({'text': {'$regex': text, '$options': 'i'}})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

@app.get('/api/products/id/<id>')
def get_products_by_id(id):
    if not ObjectId.is_valid(id):
        return abort(400, "Invalid id")

    db_id = ObjectId(id)
    product = db.products.find_one({'_id': db_id})
    if not ObjectId.is_valid(id):
        return abort(400, "Invalid id")
    
    product = fix_id(product)
    return json.dumps(product)

@app.delete('/api/products/<_id>')
def delete_products_by_id(_id):
    if not ObjectId.is_valid(_id):
        return abort(400, "Invalid id")
    
    fix_to_db_id = ObjectId(_id)
    response = db.products.delete_one({'_id': fix_to_db_id})
    if response.deleted_count == 0:
        return abort(404, 'Product not found')
    return json.dumps({'deleted': True})

#############################
#API Coupons
#############################

@app.post('/api/coupons')
def save_coupon():
    coupon = request.get_json() # This ias the object that send by client

    if not isinstance(coupon['code'],(str)):
        return abort(400, 'Code should be a String')
    
    if 'code' not in coupon or len(coupon['code']) < 3:
        return abort(400, 'Invalid code')
    
    if 'discount' not in coupon:
        return abort(400, 'Discount is empty')
    
    if not isinstance(coupon['discount'],(int,float)):
        return abort(400, 'Discount should be a number')
    
    if coupon['discount'] < 3 or coupon['discount'] > 40 :
        return abort(400, 'Discount is not within limit')

    db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

@app.get('/api/coupons')
def get_coupons():
    coupons = []
    cursor = db.coupons.find({})
    for coupon in cursor:
        coupons.append(fix_id(coupon))
    return json.dumps(coupons)

@app.get('/api/coupons/<code>')
def get_coupon_by_Code(code):
    coupon = db.coupons.find_one({'code':str(code)})
    if coupon == None:
        return abort(404, 'Coupon not found')
    return json.dumps(fix_id(coupon))

@app.delete('/api/coupons/<_id>')
def delete_coupon(_id):
    if not ObjectId.is_valid(_id):
        return abort(400, "Invalid id")
    
    fix_to_db_id = ObjectId(_id)
    response = db.coupons.delete_one({'_id': fix_to_db_id})
    if response.deleted_count == 0:
        return abort(404, 'Coupon not found')
    return json.dumps({'deleted': True})


if __name__ == '__main__':
    app.run(debug=True)