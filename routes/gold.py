import requests
import xmltodict
import json
from flask import Blueprint, jsonify, Response

gold_bp = Blueprint("gold_bp", __name__)

@gold_bp.route("/gold")
def gold_price():
    url = "http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=3kd8ub1llcg9t45hnoh8hmn7t5kc2v"

    r = requests.get(url, timeout=5)
    
    # API trả JSON → lấy luôn
    data = r.json()
    # print(data)

    items = data.get("DataList", {}).get("Data", [])
    # print(items)
    output = {
    }

    # Thời gian cập nhật cuối
    latest_time = items[0]["@d_1"]
    i=1
    for x in items:
        # print("viet:", x)
        name = x["@n_"+str(i)]
        buy = x["@pb_"+str(i)]
        sell = x["@ps_"+str(i)]
        i=i+1
        # print(i, name,buy, sell)
        output[name] = { "buy": buy, "sell": sell}
   
    return Response(
        json.dumps(output, ensure_ascii=False, indent=2), 
        mimetype='application/json'
    )