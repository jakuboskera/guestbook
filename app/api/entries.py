from flask import jsonify
from flask import make_response
from flask_restx import fields
from flask_restx import Namespace
from flask_restx import Resource

from app import db
from app.models import Entries

api = Namespace("entries", description="Entries related operations")

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


@api.route("/")
class EntryList(Resource):
    """
    Shows a list of all entries and lets you POST to add new entries
    """

    @api.doc("list_entries")
    @api.marshal_list_with(entry)
    def get(self):
        """
        List all entries
        """
        return Entries.query.order_by(Entries.created.desc()).all()

    @api.doc("create_entry")
    @api.expect(entry, validate=True)
    @api.response(201, "Created")
    def post(self, data=None):
        """
        Create a new entry
        """
        data = api.payload if data is None else data
        new_entry = Entries(data["name"], data["comment"])
        db.session.add(new_entry)
        db.session.commit()
        return make_response(jsonify("Created"), 201)


@api.route("/<int:id>")
@api.param("id", "The entry identifier")
class Entry(Resource):
    @api.doc("get_entry")
    @api.marshal_with(entry)
    def get(self, id):
        """
        Fetch a entry given its identifier
        """
        result = Entries.query.filter_by(id=id).first()
        if result is not None:
            return result
        api.abort(404, "Entry {} doesn't exist".format(id))
