import unittest

from app import create_app
from app import db
from settings import config_dict


class TestEntriesViews(unittest.TestCase):
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

    def test_entries(self):
        response = self.client.get("/entries/")
        assert b"<h4>No entries found! &#128532;</h4>" in response.data
        assert response.status_code == 200

    def test_entries_new(self):
        response = self.client.get("/entries/new")
        assert (
            b'<h5 class="card-header">Write a new entry &#129299;</h5>' in response.data
        )
        assert response.status_code == 200
