from flask import Flask
from routes.gold import gold_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(gold_bp)
    return app

app = create_app()

@app.route("/")
def home():
    return "Gold API Server is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
