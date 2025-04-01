from flask import request, jsonify
from app.controller import get_carriers, get_carriers_by_date, get_carriers_by_period
import numpy as np

def init_routes(app):


    def replace_nan_with_none(data):
        if isinstance(data, list):
            for item in data:
                for key, value in item.items():
                    if isinstance(value, float) and np.isnan(value):
                        item[key] = None
        elif isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, float) and np.isnan(value):
                    data[key] = None
        return data


    @app.route('/get', methods=['GET'])
    def get_carrier_route():
        term = request.args.get('term', '')
        if not term:
            return jsonify({"error": "Required search term"}), 400
        
        result = get_carriers(term)
        return jsonify(replace_nan_with_none(result)), 200

 
    @app.route('/carriers/date', methods=['GET'])
    def get_by_date():
        date = request.args.get('date', '')
        if not date:
            return jsonify({"error": "Date is required (format: YYYY-MM-DD)"}), 400
        
        result = get_carriers_by_date(date)
        return jsonify(replace_nan_with_none(result)), 200


    @app.route('/carriers/period', methods=['GET'])
    def get_by_period():
        start_date = request.args.get('start', '')
        end_date = request.args.get('end', '')

        if not start_date or not end_date:
            return jsonify({"error": "Both start and end dates are required (format: YYYY-MM-DD)"}), 400
        
        result = get_carriers_by_period(start_date, end_date)
        return jsonify(replace_nan_with_none(result)), 200
