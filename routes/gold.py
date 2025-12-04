import requests
import xmltodict
from flask import Blueprint, jsonify

gold_bp = Blueprint("gold_bp", __name__)

@gold_bp.route("/gold")
def gold_price():
    url = "http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=3kd8ub1llcg9t45hnoh8hmn7t5kc2v"

    r = requests.get(url, timeout=5)
    xml_data = r.text

    # Parse XML → dict
    data = xmltodict.parse(xml_data)
    items = data.get("DataList", {}).get("Data", [])

    # Ensure items is list
    if isinstance(items, dict):
        items = [items]

    # Convert attributes
    parsed = [item["@"] for item in items]

    # Tìm lần cập nhật mới nhất
    latest_time = parsed[0].get("d_1", "")

    # Map tên vàng → JSON đẹp
    output = {
        "sjc": None,
        "vrtl": None,
        "qua_mung": None,
        "nhan_tron": None,
        "btmc_9999": None,
        "btmc_999": None,
        "nguyen_lieu": None
    }

    for x in parsed:
        name = x.get("n_1") or ""

        if "SJC" in name:
            output["sjc"] = {
                "name": "Vàng miếng SJC",
                "buy": int(x.get("pb_1")),
                "sell": int(x.get("ps_1"))
            }

        elif "Rồng Thăng Long" in name and "Miếng" in name:
            output["vrtl"] = {
                "name": "Vàng Rồng Thăng Long",
                "buy": int(x.get("pb_1")),
                "sell": int(x.get("ps_1"))
            }

        elif "Quà Mừng" in name:
            output["qua_mung"] = {
                "name": "Quà mừng bản vị vàng",
                "buy": int(x.get("pb_1")),
                "sell": int(x.get("ps_1"))
            }

        elif "Nhẫn Tròn" in name:
            output["nhan_tron"] = {
                "name": "Nhẫn tròn trơn",
                "buy": int(x.get("pb_1")),
                "sell": int(x.get("ps_1"))
            }

        elif "99.9" in name:
            output["btmc_999"] = {
                "name": "Trang sức BTMC 99.9",
                "buy": int(x.get("pb_1")),
                "sell": int(x.get("ps_1"))
            }

        elif "999.9" in name:
            output["btmc_9999"] = {
                "name": "Trang sức BTMC 999.9",
                "buy": int(x.get("pb_1")),
                "sell": int(x.get("ps_1"))
            }

        elif "Nguyên Liệu" in name:
            output["nguyen_lieu"] = {
                "name": "Vàng nguyên liệu",
                "buy": int(x.get("pb_1")),
                "sell": int(x.get("ps_1"))
            }

    return jsonify({
        "updated": latest_time,
        "prices": output
    })
