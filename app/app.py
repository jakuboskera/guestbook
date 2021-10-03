import os

from api import blueprint
from flask import Flask
from flask_migrate import Migrate
from models import db
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="/api/v1")
app.config["SWAGGER_UI_DOC_EXPANSION"] = "list"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# if deployed to Heroku, env var DATABASE_URL is used
conn = os.environ.get("DATABASE_URL")
if conn is not None:
    if conn and conn.startswith("postgres://"):
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

app.config["SQLALCHEMY_DATABASE_URI"] = conn

db.init_app(app)
migrate = Migrate(app, db)

if os.environ.get("PROMETHEUS_METRICS") != "disable":
    PrometheusMetrics(app)

from views import *

if __name__ == "__main__":

    app.run(port=int(os.environ.get("PORT", 5000)))
