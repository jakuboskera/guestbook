import unittest

from app import create_app
from settings import config_dict


class TestErrorViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict["test"])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.client = None

    def test_error_404(self):
        response = self.client.get("/non-existing-page")
        assert b"<h4>Page not found! &#129335;</h4>" in response.data
        assert response.status_code == 404
