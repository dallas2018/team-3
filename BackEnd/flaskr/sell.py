import functools
import requests
import json
import base64
import os
from bson import json_util

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

REDIRECT_URI = 'soundhub://callback'


bp = Blueprint('sell', __name__, url_prefix='/sell')

@bp.route('/', methods=('GET', 'POST'))
def getAllProductsForBuyPage():
    # returns a json file that contains all the products to display
    print(mongo)
    x = [json.dumps(y, default=json_util.default) for y in mongo.db.Users.find({})]
    print(x)

    return 'selling../'


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
    add it to the transaction db
    return status
    '''
    if request.method == 'GET':
        return {status: 404, err: " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "}
    
    name = request.form['name']
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    file.save(f)

    return "workeddd"
