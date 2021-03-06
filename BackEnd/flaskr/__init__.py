import os
from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/charityMarket"
    mongo = PyMongo(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_URI= "mongodb://localhost:27017/charityMarket"
    )

    mongo = PyMongo(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import charity
    app.register_blueprint(charity.bp)

    from . import acc
    app.register_blueprint(acc.bp)
    
    from . import buy
    app.register_blueprint(buy.bp)
    
    from . import sell
    app.register_blueprint(sell.bp)

    from . import addUser
    app.register_blueprint(addUser.bp)

    # json_data = json.load(open("flaskr/charityQuery.json"))
    # hits = json_data["data"]["hits"]
    # x = [json.loads(json.dumps(y, default=json_util.default)) for y in hits]
    # mongo.db.Charities.insert_many((x))

    @app.route('/')
    def hello():
        #     online_users = mongo.db.users.find({"online": True})
        return 'Welcome to MarketPlace'

    return app