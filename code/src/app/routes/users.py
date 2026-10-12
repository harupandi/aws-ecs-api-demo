from flask import Blueprint, jsonify

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.get("/")
def list_users():
    return jsonify([])

@bp.get("/<int:user_id>")
def get_user(user_id):
    return jsonify({"id": user_id})