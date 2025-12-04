import requests
from flask import Blueprint, jsonify

gold_bp = Blueprint("gold", __name__)

@gold_bp.get("/gold")
def get_gold():
    try:
        data = requests.get("https://api.exchangerate.host/latest?base=XAU&symbols=USD").json()
        return jsonify({"price": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
