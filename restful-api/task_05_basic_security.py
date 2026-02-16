#!/usr/bin/env python3
"""
Flask API with Basic Auth, JWT Auth, and Role-Based Access Control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# 🔐 Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# 👥 In-memory users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

# =========================================================
# 🔐 BASIC AUTH
# =========================================================

@auth.verify_password
def verify_password(username, password):
    """Verify basic auth credentials"""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """Return 401 for all basic auth errors"""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Basic Auth protected route"""
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


# =========================================================
# 🔐 JWT ERROR HANDLERS → MUST RETURN 401
# =========================================================

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401


# =========================================================
# 🔑 LOGIN → RETURN JWT TOKEN
# =========================================================

@app.route("/login", methods=["POST"])
def login():
    """Login and return JWT token"""
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 401

    user = users.get(data["username"])

    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # Store username and role inside token
    access_token = create_access_token(
        identity={"username": user["username"], "role": user["role"]}
    )

    return jsonify({"access_token": access_token}), 200


# =========================================================
# 🔐 JWT PROTECTED ROUTE
# =========================================================

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """JWT protected route"""
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


# =========================================================
# 🛡️ ADMIN ONLY ROUTE
# =========================================================

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin role required"""
    current_user = get_jwt_identity()

    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200


# =========================================================
# 🚀 RUN APP
# =========================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

