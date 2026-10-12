from flask import Blueprint
from .users import bp as users_bp
from .transactions import bp as transactions_bp

api = Blueprint("api", __name__, url_prefix="/api")

api.register_blueprint(users_bp)
api.register_blueprint(transactions_bp)