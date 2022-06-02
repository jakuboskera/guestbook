import unittest

from app import create_app
from settings import config_dict


class TestMainViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict["test"])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.client = None

    def test_home(self):
        response = self.client.get("/")
        assert b'<h1 class="display-4">Hello &#128075;</h1>' in response.data
        assert response.status_code == 200
