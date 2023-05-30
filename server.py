from flask import Flask, render_template
import json

app = Flask(__name__)

@app.get('/')
def home():
    return "Hello, this is a home page"

@app.get('/test')
def test():
    return "Hello from another page"

@app.get('/about')
def about():
    me = {'name:': 'Rafael'}
    return json.dumps(me)


app.run(debug=True)

