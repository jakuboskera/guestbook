import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # if deployed to Heroku, env var DATABASE_URL is used
    conn = os.environ.get("DATABASE_URL")
    if conn is not None:
        if conn.startswith("postgres://"):
            conn = conn.replace("postgres://", "postgresql://", 1)
    else:
        conn = (
            "postgresql://"
            + os.environ.get("DB_USER", "")
            + ":"
            + os.environ.get("DB_PASSWORD", "")
            + "@"
            + os.environ.get("DB_HOST", "")
            + ":"
            + os.environ.get("DB_PORT", "")
            + "/"
            + os.environ.get("DB_NAME", "")
        )

    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=conn,
        SWAGGER_UI_DOC_EXPANSION="list",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)

    if os.environ.get("PROMETHEUS_METRICS") != "disable":
        PrometheusMetrics(app)

    from app.main.views import blueprint as main
    from app.api import blueprint as api
    from app.entries.views import blueprint as entries
    from app.health.views import blueprint as health

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api/v1")
    app.register_blueprint(entries, url_prefix="/entries")
    app.register_blueprint(health, url_prefix="/health")

    from app.main.errors import page_not_found

    app.register_error_handler(404, page_not_found)

    return app
