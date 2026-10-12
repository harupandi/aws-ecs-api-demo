from flask import Blueprint, jsonify

bp = Blueprint("transactions", __name__, url_prefix="/transactions")

@bp.get("/")
def list_transactions():
    return jsonify([])

@bp.get("/<int:transaction_id>")
def get_transaction(transaction_id):
    return jsonify({"id": transaction_id})