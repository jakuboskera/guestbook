import os


class Config(object):
    """Base configuration"""

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    PROMETHEUS_METRICS = os.environ.get("PROMETHEUS_METRICS", "enable")


class ProductionConfig(Config):
    """Production configuration"""

    # if deployed to Heroku, injected env var DATABASE_URI is used
    conn = os.environ.get("DATABASE_URI")
    if conn is None:
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
    else:
        if conn.startswith("postgres://"):
            conn = conn.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = conn

class TestingConfig(Config):
    """Testing configuration"""

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    DB_NAME = "dev.db"
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}".format(DB_PATH)


config_dict = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}
