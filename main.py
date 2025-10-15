from flask import Flask, request, jsonify

app = Flask(__name__)

SECRET = "mytdssecret2025"

@app.route("/api-endpoint", methods=["POST"])
def receive_task():
    data = request.get_json()
    print("Received:", data)

    # Verify secret
    if not data or data.get("secret") != SECRET:
        return jsonify({"ok": False, "error": "Invalid secret"}), 403

    return jsonify({"ok": True, "message": "Request received and verified!"}), 200

if __name__ == "__main__":
    app.run(port=5000)
