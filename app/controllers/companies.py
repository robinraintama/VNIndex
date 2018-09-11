import os
import sys
import json
import re
from flask import request, jsonify, Response                     
from app import app, mongo
from bson import json_util
# import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
# LOG = logger.get_root_logger(
#     __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/companies', methods=['GET'])
def companies():
    ''' route read companies '''

    # Default Parameters
    find_param = {}
    remove_id_param = {'_id': 0}
    data = {}
    code = 200
    message = "successful"

    # Validate request parameter
    # Filter company name
    # Implement contains & ignore case
    if request.args.get('company_name') is not None:
    	find_param['company name'] = re.compile(request.args.get('company_name'), re.IGNORECASE)

    # Filter company business where value equals parameter
    if request.args.get('industry') is not None:
    	find_param['business'] = request.args.get('business')

    # Filter company revenue where market cap greater than parameter
    # Handle ValueError when parameter is not int
    if request.args.get('revenue_gte') is not None:
        try:
        	revenue = int(request.args.get('revenue_gte'))
        	find_param['financial summary.Market Cap'] = {'$gte':revenue}
        except ValueError:
            # return error code page
            code = 204
            message = "failed because of revenue parameter not integer"
            find_param = {"_id":0}
            print("ValueError revenue_gte")

    # Query MongoDB with parameters
    data = mongo.db.company_profile.find(find_param,remove_id_param)
    
    # Convert MongoDB selector into JSON String
    data_lists = list(data)

    response = {
    	"status_code": code,
    	"message": message,
    	"data": data_lists
    	}

    response = json.dumps(response, default=json_util.default)

    return Response(response, status=code, mimetype='application/json')