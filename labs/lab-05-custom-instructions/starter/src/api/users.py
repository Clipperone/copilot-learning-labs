from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store — not for production use
_users = {}


def get_user(user_id):
    user = _users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "not found"}), 404


def create_user():
    data = request.json
    user_id = data["id"]
    _users[user_id] = data
    return jsonify(data), 201


def delete_user(user_id):
    if user_id not in _users:
        return jsonify({"error": "not found"}), 404
    del _users[user_id]
    return jsonify({}), 204
