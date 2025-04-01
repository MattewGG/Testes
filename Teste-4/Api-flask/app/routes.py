from flask import request, jsonify
from app.controller import get_carriers
import pandas as pd  
import numpy as np

def init_routes(app):

    @app.route('/get', methods=['GET'])
    def get_carrier_route():
            term = request.args.get('term', '')
            if not term:
                return jsonify({"error": "Required search term"}), 400
            
            result = get_carriers(term)


            if isinstance(result, list):
                for item in result:
                    for key, value in item.items():
                        if isinstance(value, float) and np.isnan(value):
                            item[key] = None  
            elif isinstance(result, dict):
                for key, value in result.items():
                    if isinstance(value, float) and np.isnan(value):
                        result[key] = None  
            return jsonify(result)

    