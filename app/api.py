from flask import Blueprint
from flask import jsonify
from flask import make_response
from flask_restx import Api
from flask_restx import fields
from flask_restx import Namespace
from flask_restx import Resource
from models import db
from models import EntriesModel


blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, title="Guestbook", version="1.0", description="Guestbook simple API"
)

ns = Namespace("entries", description="Entries related operations")
api.add_namespace(ns)

entry = api.model(
    "Entry",
    {
        "id": fields.Integer(readonly=True, description="The entry identifier"),
        "name": fields.String(required=True, description="The entry name"),
        "comment": fields.String(required=True, description="The entry comment"),
        "created": fields.DateTime(
            readonly=True, description="The date of submitted entry"
        ),
    },
)


@ns.route("/")
class EntryList(Resource):
    """
    Shows a list of all entries and lets you POST to add new entries
    """

    @ns.doc("list_entries")
    @ns.marshal_list_with(entry)
    def get(self):
        """
        List all entries
        """
        return EntriesModel.query.order_by(EntriesModel.created.desc()).all()

    @ns.doc("create_entry")
    @ns.expect(entry, validate=True)
    def post(self, data=None):
        """
        Create a new entry
        """
        data = ns.payload if data is None else data
        new_entry = EntriesModel(data["name"], data["comment"])
        db.session.add(new_entry)
        db.session.commit()
        return make_response(jsonify(created=True), 201)


@ns.route("/<int:id>")
@ns.param("id", "The entry identifier")
class Entry(Resource):
    @ns.doc("get_entry")
    @ns.marshal_with(entry)
    def get(self, id):
        """
        Fetch a entry given its identifier
        """
        result = EntriesModel.query.filter_by(id=id).first()
        if result is not None:
            return result
        api.abort(404, "Entry {} doesn't exist".format(id))
