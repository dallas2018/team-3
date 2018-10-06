import functools
import requests
import json
import base64
from flask import (
    Blueprint, redirect, request, jsonify
)

bp = Blueprint('charity', __name__, url_prefix='/charity')

@bp.route('/', methods=('GET', 'POST'))
def printHello():
    return('This is the Charity')

@bp.route('/addCharity', methods=('GET', 'POST'))
def addCharity():
    return 'Nothing Yet'

@bp.route('/delCharity', methods=('GET', 'POST'))
def delCharity():
    return 'Nothing Yet'

@bp.route('/getCharityInfo', methods=('GET', 'POST'))
def getCharityInfo():
    return 'Nothing Yet'


