from flask import Flask
from routes.gold import gold_bp

app = Flask(__name__)
app.register_blueprint(gold_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
