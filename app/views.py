import health
from api import EntryList
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app import app


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("pages/index.html")


@app.route("/entries")
def entries():
    """
    List of entries.
    """
    return render_template(
        "pages/entries/index.html",
        entries=EntryList().get(),
        title="Entries - ",
    )


@app.route("/entries/new")
def new_entry():
    """
    Form for new entry.
    """
    return render_template("pages/entries/new.html", title="Add a new entry - ")


@app.route("/entries/new", methods=["POST"])
def post_entry():
    """
    Accepts POST requests, and processes the form;
    Redirect to entries when completed.
    """
    data = {
        "name": request.form.get("name", "Anonymous"),
        "comment": request.form["comment"],
    }
    EntryList().post(data)
    return redirect(url_for("entries"))


# liveness probe
@app.route("/health")
def health_live():
    return jsonify(health.liveness_probe())


# readiness probe
@app.route("/health/ready")
def health_ready():
    if health.readiness_probe():
        return jsonify({"status": "ready"})
    else:
        return jsonify({"status": "not ready"}), 500


@app.errorhandler(404)
def page_not_found(e):
    """
    Requested non-existing page.
    """
    return render_template("pages/404.html"), 404
