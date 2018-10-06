import functools
import requests
import json
import base64
from flask import (
    Blueprint, redirect, request, jsonify
)

bp = Blueprint('acc', __name__, url_prefix='/acc')

@bp.route('/', methods=('GET', 'POST'))
def printHello():
    return('This is the Accounts Endpoint')

@bp.route('/getAccInfo', methods=('GET', 'POST'))
def getAccInfo():
    ''' Request Type: POST - Input: User Auth Token - Output: JSON of Account Info '''
    if request.method == 'GET':
        return " ERROR 404 - GET REQUESTS NOT SERVICED AT THIS ENDPOINT "



    return 'Nothing Yet'

