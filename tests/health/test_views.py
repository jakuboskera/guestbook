import unittest

from app import create_app
from app import db
from settings import config_dict


class TestHealthViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict["test"])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.client = None

    def test_health(self):
        response = self.client.get("/health/")
        assert b'"status": "success"' in response.data
        assert response.status_code == 200
