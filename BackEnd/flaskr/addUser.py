import functools
import requests
import json
import base64
import os
from bson import json_util
import uuid

# from urllib.parse import urlencode
from flask import (
    Blueprint, redirect, request, jsonify, Flask,render_template
)
from flask_pymongo import PyMongo

app = Flask(__name__, instance_relative_config=True)


app.config["MONGO_URI"] = "mongodb://localhost:27017/charityMarket"

mongo = PyMongo(app)

REDIRECT_URI = 'soundhub://callback'


bp = Blueprint('addUser', __name__, url_prefix='/addUser')

@bp.route('/', methods=('GET', 'POST'))
def addUser():
    # returns a json file that contains all the products to display
    a = request.form['authId']
    b = request.form['name']

    mongo.db.Users.insert({'authId': a, 'name': b, 'favCharities': [], 'transactions': [], 'donations':[], 'currentProducts':[]})

    return jsonify({'success': True})