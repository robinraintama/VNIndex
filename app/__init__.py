#app/__init__.py

import os
import json
import datetime
from bson.objectid import ObjectId
from flask import Flask
from flask_pymongo import PyMongo

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)

# # add mongo url to flask config, so that flask_pymongo can use it to make connection
# app.config['MONGO_DBNAME'] = 'vnindex_db'
# app.config['MONGO_URI'] = os.environ.get('DB')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/vnindex_db'

mongo = PyMongo(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder

from app.controllers import *