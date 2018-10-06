import functools
import requests
import json
import base64
from flask import (
    Flask, Blueprint, redirect, request, jsonify
)
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/charityMarket"
mongo = PyMongo(app)

bp = Blueprint('charity', __name__, url_prefix='/charity')

@bp.route('/', methods=('GET', 'POST'))
def printHello():
    return('This is the Charity Endpoint')

@bp.route('/addFav', methods=('GET', 'POST'))
def addFav():
    ''' Request Type: POST - Input: User Auth Token, Charity ID - Output: Status of Success '''
    if request.method == 'GET':
        return " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "
    authToken = request.form['authToken']
    charityId = request.form['charityId']
    mongo.db.Users.findOneandUpdate({'authId', authToken}, {'$addToSet': {'favCharities': [charityId]}})
    return 'Inserted'

@bp.route('/delFav', methods=('GET', 'POST'))
def delFav():
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
