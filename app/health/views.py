from flask import Blueprint
from healthcheck import HealthCheck

from app import db


blueprint = Blueprint("health", __name__, template_folder="templates")
health = HealthCheck()


def postgres_available():
    """
    Return True and "postgres ok" if connection to postgres is successfull
    """
    is_db_ok = True
    output = "postgres ok"

    try:
        db.session.execute("SELECT 1")
    except Exception as e:
        output = str(e)
        is_db_ok = False

    return is_db_ok, output


health.add_check(postgres_available)
blueprint.add_url_rule("/", "health", view_func=health.run)
