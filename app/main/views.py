from flask import Blueprint
from flask import render_template

blueprint = Blueprint("main", __name__, template_folder="templates")


@blueprint.route("/")
def home():
    return render_template("index.html")
