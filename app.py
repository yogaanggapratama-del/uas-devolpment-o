from flask import Flask, jsonify, request

app = Flask(__name__)
stock = {"ITEM001": 50, "ITEM002": 20}

@app.route("/api/items")
def get_items():
    return jsonify(stock)

@app.route("/api/items/<item_id>/reduce", methods=["POST"])
def reduce_stock(item_id):
    qty = request.json.get("quantity", 0)
    if item_id not in stock:
        return jsonify({"error": "item not found"}), 404
    if stock[item_id] < qty:
        return jsonify({"error": "stock tidak cukup"}), 400
    stock[item_id] -= qty
    return jsonify({"item_id": item_id, "stock": stock[item_id]})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)