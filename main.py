from flask import Flask
from routes.gold import gold_bp

# MCP imports
from mcp.server.flask import FlaskApp
from mcp import tool, types

def create_app():
    app = Flask(__name__)
    app.register_blueprint(gold_bp)

    # ============================
    #     MCP SERVER FOR CHATGPT
    # ============================
    mcp_server = FlaskApp("gold-mcp")

    @tool
    def gold():
        """Lấy giá vàng mới nhất (MCP Tool)."""
        from routes.gold import get_gold_price  # import tại đây tránh circular
        return types.JSONResponse(get_gold_price())

    # Mount MCP vào /mcp
    app.register_blueprint(mcp_server.blueprint, url_prefix="/mcp")

    return app


app = create_app()

@app.route("/")
def home():
    return "Gold API + MCP Server is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
