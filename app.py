from flask import Flask, request, jsonify
from auth import register_user, login_user
import jwt

app = Flask(__name__)
SECRET_KEY = "supersecretkey"

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    success, message = register_user(
        data["username"],
        data["password"],
        data.get("role", "user")
    )
    return jsonify({"message": message})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    success, result = login_user(data["username"], data["password"])
    if success:
        return jsonify({"token": result})
    return jsonify({"message": result}), 401

@app.route("/protected", methods=["GET"])
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token missing"}), 403

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({
            "message": "Access granted",
            "user": decoded["username"],
            "role": decoded["role"]
        })
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 403
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 403

@app.route("/admin", methods=["GET"])
def admin_only():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token missing"}), 403

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if decoded["role"] != "admin":
            return jsonify({"message": "Admin access only"}), 403

        return jsonify({"message": "Welcome Admin"})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 403
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 403

if __name__ == "__main__":
    app.run(debug=True)
