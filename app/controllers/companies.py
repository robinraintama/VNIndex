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

    find_param = {}
    remove_id_param = {'_id': 0}

    if request.args.get('company_name') is not None:
    	find_param['company name'] = request.args.get('company_name')
    if request.args.get('business') is not None:
    	find_param['business'] = request.args.get('business')
    if request.args.get('revenue_gte') is not None:
    	revenue = int(request.args.get('revenue_gte'))
    	find_param['financial summary.Market Cap'] = {'$gte':revenue}

    print(find_param)
    data = mongo.db.company_profile.find(find_param,remove_id_param)
    data_lists = list(data)
    data_response = json.dumps(data_lists, default=json_util.default)
    return data_response, 200