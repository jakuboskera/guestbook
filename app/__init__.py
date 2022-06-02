from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import config_dict

db = SQLAlchemy()


def create_app(config=config_dict["dev"]):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    if app.config.get("PROMETHEUS_METRICS") == "enable":
        from prometheus_flask_exporter import PrometheusMetrics

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
