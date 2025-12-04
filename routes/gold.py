import requests
from flask import Blueprint, jsonify

gold_bp = Blueprint("gold", __name__)

@gold_bp.get("/gold")
def get_gold():
    try:
        data = requests.get("http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=3kd8ub1llcg9t45hnoh8hmn7t5kc2v").json()
        return jsonify({"price": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
