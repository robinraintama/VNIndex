import os
import sys
import json
from flask import request, jsonify                       
from app import app, mongo
from bson import json_util
# import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
# LOG = logger.get_root_logger(
#     __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/companies', methods=['GET'])
def companies():
    ''' route read companies '''
    if request.method == 'GET':
        data = mongo.db.company_profile.find({},{'_id': 0})
        data_lists = list(data)
        data_response = json.dumps(data_lists, default=json_util.default)
        return data_response, 200