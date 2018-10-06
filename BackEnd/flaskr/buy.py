import functools
import requests
import json
import base64
from flask_pymongo import PyMongo
from bson import json_util
from flask import (
    Flask, Blueprint, redirect, request, jsonify
)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/charityMarket"
mongo = PyMongo(app)

bp = Blueprint('buy', __name__, url_prefix='/buy')

@bp.route('/getSellables', methods=('GET', 'POST'))
def getSellables():
    # returns a json file that contains all the products to display
    products = mongo.db.Products.find()
    x = [json.loads(json.dumps(y, default=json_util.default)) for y in products]
    return str(x)

@bp.route('/buyItem', methods=('GET', 'POST'))
def getAllProductsForBuyPages():
    ''' input: /buy?productId=12
        remove the item from owner's live sell list
        remove the item from buy list
        add it to the transcation of the buyer
        add it to the transcation of the seller
        refresh the client home page
    '''
    
    # returns a json file that contains all the products to display
    # productId =  request.args.get('productId')
    pass
