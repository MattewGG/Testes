from flask import request, jsonify
from app.controller import get_carriers

def init_routes(app):
    @app.route('/get', methods=['GET'])
    def get_carrier_route():
        term = request.args.get('term', '')
        if not term:
            return jsonify({"erro": "Required search term"}), 400
        result = get_carriers(term)
        return jsonify(result)
