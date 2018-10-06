import functools
import requests
import json
import base64
from bson import json_util
from flask import (
    Blueprint, redirect, request, jsonify, Flask
)
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/charityMarket"
mongo = PyMongo(app)

from flask_pymongo import PyMongo
app = Flask(__name__, instance_relative_config=True)
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

    authId = request.form['authId']
    charityId = request.form['charityId']
    mongo.db.Users.find_one_and_update({'authId': authId}, {'$addToSet': {'favCharities': charityId}})
    return jsonify({ 'success': True })

@bp.route('/delFav', methods=('GET', 'POST'))
def delFav():
    ''' Request Type: POST - Input: User Auth Token, Charity ID - Output: Status of Success '''
    if request.method == 'GET':
        return " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "

    authId = request.form['authId']
    charityId = request.form['charityId']
    mongo.db.Users.find_one_and_update({'authId': authId}, {'$pull': {'favCharities': charityId}})

    return jsonify({ 'success': True })

@bp.route('/getCharities', methods=('GET', 'POST'))
def getCharityInfo():
    ''' Request Type: Post - Input: User Auth Token - Output: List of All Charities
        and Favorites of selected user '''
    if request.method == 'POST':
        return " ERROR 404 - POST REQUESTS NOT SERVICED AT THIS ENDPOINT "

    json_data = json.load(open("flaskr/charityQuery.json"))
    return jsonify(json_data)