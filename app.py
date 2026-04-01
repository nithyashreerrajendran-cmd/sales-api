from flask import Flask, jsonify
from src.loader import load_sales

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Sales API is running! ✅"})

@app.route("/sales", methods=["GET"])
def get_sales():
    df = load_sales()
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)