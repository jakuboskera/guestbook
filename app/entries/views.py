from dateutil import parser
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app.api.entries import EntryList


blueprint = Blueprint("entries", __name__, template_folder="templates")


@blueprint.route("/")
def show_entries():
    """
    List of entries.
    """
    return render_template("show_entries.html", entries=EntryList().get())


@blueprint.route("/new", methods=["GET", "POST"])
def new_entry():
    """
    Form for new entry.
    """
    if request.method == "POST":
        data = {
            "name": request.form.get("name", "Anonymous"),
            "comment": request.form["comment"],
        }
        EntryList().post(data)
        return redirect(url_for("entries.show_entries"))
    return render_template("new.html")


@blueprint.app_template_filter("strftime")
def _jinja2_filter_datetime(date, fmt=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    format = "%b %d, %Y"
    return native.strftime(format)
