from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/send", methods=["POST"])
def send():
    data = request.json

    messages.append({
        "sender": data["sender"],
        "message": data["message"]
    })

    return jsonify({
        "success": True
    })

@app.route("/messages")
def get_messages():
    return jsonify(messages)

app.run(host="0.0.0.0", port=3000)
