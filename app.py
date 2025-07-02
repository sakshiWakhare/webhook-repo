from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data.get("action") == "closed" and data.get("pull_request", {}).get("merged"):
        print("A Pull Request was merged!")
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run(port=5000)
