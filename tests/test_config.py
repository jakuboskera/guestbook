from app import create_app
from settings import DevelopmentConfig
from settings import ProductionConfig
from settings import TestingConfig


class TestConfig:
    def test_production_config(self):
        """Production config."""

        app = create_app(ProductionConfig)
        assert not app.config["DEBUG"]
        assert app.config["TESTING"] == False

    def test_test_config(self):
        """Testing config."""

        app = create_app(TestingConfig)
        assert app.config["DEBUG"] == True
        assert app.config["TESTING"] == True

    def test_dev_config(self):
        """Development config."""

        app = create_app(DevelopmentConfig)
        assert app.config["DEBUG"] == True
        assert app.config["TESTING"] == False
