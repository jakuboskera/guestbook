from flask import render_template

from app.main.views import blueprint


@blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404
