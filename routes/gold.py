from flask import Blueprint, jsonify
import requests
import xml.etree.ElementTree as ET

gold_blueprint = Blueprint("gold", __name__)

@gold_blueprint.route("/gold")
def get_gold_price():
    url = "http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=3kd8ub1llcg9t45hnoh8hmn7t5kc2v"
    r = requests.get(url)
    root = ET.fromstring(r.text)

    data = []
    for item in root.findall("Data"):
        entry = item.attrib
        data.append(entry)

    return jsonify({"data": data})
