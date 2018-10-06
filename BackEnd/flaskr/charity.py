import functools
import requests
import json
import base64
from flask import (
    Blueprint, redirect, request, jsonify, Flask
)

from flask_pymongo import PyMongo
app = Flask(__name__, instance_relative_config=True)
app.config["MONGO_URI"] = "mongodb://localhost:27017/charityMarket"
mongo = PyMongo(app)

bp = Blueprint('charity', __name__, url_prefix='/charity')

@bp.route('/', methods=('GET', 'POST'))
def printHello():
    return('This is the Charity Endpoint')

@bp.route('/addFav', methods=('GET', 'POST'))
def addCharity():
    ''' Request Type: POST - Input: User Auth Token - Output: Status of Success '''
    if request.method == 'GET':
        return " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "



    return 'Nothing Yet'

@bp.route('/delFav', methods=('GET', 'POST'))
def delCharity():
    ''' Request Type: POST - Input: User Auth Token - Output: Status of Success '''
    if request.method == 'GET':
        return " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "



    return 'Nothing Yet'

@bp.route('/getCharitys', methods=('GET', 'POST'))
def getCharityInfo():
    ''' Request Type: Post - Input: User Auth Token - Output: List of All Charities
        and Favorites of selected user '''
    if request.method == 'GET':
        return " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "
    
    

    return 'Nothing Yet'
