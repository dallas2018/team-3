import functools
import requests
import json
import base64
# from urllib.parse import urlencode

from flask import (
    Blueprint, redirect, request, jsonify
)

REDIRECT_URI = 'soundhub://callback'


bp = Blueprint('buy', __name__, url_prefix='/buy')

@bp.route('/', methods=('GET', 'POST'))
def getAllProductsForBuyPage():
    # returns a json file that contains all the products to display
    pass

@bp.route('/buy', methods=('GET', 'POST'))
def getAllProductsForBuyPage():
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
