from flask import Blueprint
from flask_restx import Api

from app.api.entries import api as entries

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, title="Guestbook", version="1.0", description="Guestbook simple API"
)

api.add_namespace(entries)
