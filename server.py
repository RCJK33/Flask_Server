from flask import Flask, request
import json
from config import db

app = Flask(__name__)

@app.get('/')
def home():
    return "Hello, this is a home page"

@app.get('/test')
def test():
    return '<a href="/about ">fdsfdsf<a/>'

@app.get('/api/about')
def about():
    me = {'name:': 'Rafael'}
    return json.dumps(me)


#############################
# API endpoints
# JSON
#############################

def fix_id(obj):
    obj['_id'] = str(obj['_id'])
    return obj

@app.get('/api/version')
def version():
    version = {
        'name': 'mouse',
        'version': 35,
        'build': 2948
    }
    return json.dumps(version)

@app.get('/api/products')
def get_products():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

@app.post('/api/products')
def save_product():
    data = request.get_json() # This ias the object that send by client 
    db.products.insert_one(data)

    # products.append(data)
    print(data)
    return json.dumps(fix_id(data))

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
        categories.add(str(prod['category']).lower())
    categories = list(categories)
    categories.sort()
    return json.dumps(categories)


app.run(debug=True)