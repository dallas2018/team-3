import functools
import requests
import json
import base64
import os
from bson import json_util
import uuid
import random
import string

# from urllib.parse import urlencode
from flask import (
    Blueprint, redirect, request, jsonify, Flask,render_template
)
from flask_pymongo import PyMongo

UPLOAD_FOLDER = os.path.basename('/static/')

app = Flask(__name__, instance_relative_config=True)


app.config["MONGO_URI"] = "mongodb://localhost:27017/charityMarket"
app.config['UPLOAD_FOLDER'] = 'static/'

mongo = PyMongo(app)

bp = Blueprint('sell', __name__, url_prefix='/sell')

# @bp.route('/', methods=('GET', 'POST'))
# def getAllProductsForBuyPage():
#     # returns a json file that contains all the products to display
#     print(mongo)
#     x = [json.dumps(y, default=json_util.default) for y in mongo.db.Users.find({})]
#     print(x)

#     return 'selling../'


@bp.route('/getSellValue', methods=('GET', 'POST'))
def getSellValue():
    # POST
    '''
    input: get a image from body.
     try to find the value if possible
     return the possible value
    '''
    # returns a json with the name and value of the image (product)
    pass

@bp.route('/sellProduct', methods=('GET', 'POST'))
def sell():
    '''
    input: name, image, price, description, charities
    store the produce in the product list
    add the product to the live owner's live list
    return status
    '''
    if request.method == 'GET':
        return jsonify({status: 404, err: " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "})
    
    name = request.form['name']
    file = request.files['image']
    price = int(request.form['price'])
    authId = request.form['authId']
    new_file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)) +'.' + file.filename.split('.')[1]
    f = os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)    
    file.save(f)

    p_id = str(uuid.uuid1())
    
    mongo.db.Products.insert({'productId': p_id, 'name': name, 'price': price, 'address': f, 'owner': authId})
    mongo.db.Users.find_one_and_update({'authId': authId}, {'$addToSet': {'currentProducts': p_id}})
    

    return jsonify({'status': 'posted successfully'})
