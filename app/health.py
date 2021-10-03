from healthcheck import HealthCheck
from models import db

from app import app


health = HealthCheck()


def is_postgres_available():
    """
    Return True and "postgres ok" if connection to postgres is sucessfull
    """
    is_db_ok = True
    output = "postgres ok"

    try:
        db.session.execute("SELECT 1")
    except Exception as e:
        output = str(e)
        is_db_ok = False

    return is_db_ok, output


health.add_check(is_postgres_available)
app.add_url_rule("/health", "health", view_func=health.run)
