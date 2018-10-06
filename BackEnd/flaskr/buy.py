import functools
import requests
import json
import base64
import uuid
from flask_pymongo import PyMongo
from bson import json_util
from flask import (
    Flask, Blueprint, redirect, request, jsonify
)

from flask_pymongo import PyMongo
app = Flask(__name__, instance_relative_config=True)
mongo = PyMongo(app)

REDIRECT_URI = 'soundhub://callback'

bp = Blueprint('buy', __name__, url_prefix='/buy')

@bp.route('/getSellables', methods=('GET', 'POST'))
def getSellables():
    # returns a json file that contains all the products to display
    if request.method == 'POST':
        return " ERROR 404 - POST REQUESTS NOT SERVICED AT THIS ENDPOINT "
    products = mongo.db.Products.find()
    x = [json.loads(json.dumps(y, default=json_util.default)) for y in products]
    return str(x)

@bp.route('/buyItem', methods=('GET', 'POST'))
def buyItemfl():
    ''' input: productId, UserID
        remove the item from owner's live sell list
        remove the item from buy list
        add it to the transcation of the buyer
        add it to the transcation of the seller
        refresh the client home page
    '''
    if request.method == 'GET':
        return " ERROR 404 - POST REQUESTS NOT SERVICED AT THIS ENDPOINT "
    productId = request.form["productId"]
    authId = request.form["authId"]
    transactionId = uuid.uuid1()

    mongo.db.Users.find_one_and_update({'authId': authId}, {'$addToSet': {'transaction': transactionId}})

    itemObject = mongo.db.Products.find_one({'productId': productId})
    mongo.db.Users.find_one_and_update({'authId': itemObject['owner']}, {'$pull': {'currentProducts': productId}})
    mongo.db.Users.find_one_and_update({'authId': itemObject['owner']}, {'$addToSet': {'transactions': transactionId}})
    
    mongo.db.Products.delete_one({'productId': productId})
    mongo.db.Transaction.insert_one({'t_id': transactionId, 'price': itemObject['price'], 'owner': itemObject['owner'], 'buyer': authId})

    return jsonify({ 'success': True })