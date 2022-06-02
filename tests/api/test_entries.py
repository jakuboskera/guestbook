import datetime
import unittest

from dateutil import parser

from app import create_app
from app import db
from settings import config_dict


class TestApiEntries(unittest.TestCase):
    ENTRY = {"name": "Anonymous", "comment": "Guestbook is awesome"}

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

    def test_get_entries(self):
        response = self.client.get("/api/v1/entries/")
        assert response.json == []
        assert response.status_code == 200

    def test_post_entry(self):
        response = self.client.post("/api/v1/entries/", json=self.ENTRY)
        assert response.json == "Created"
        assert response.status_code == 201

    def test_get_created_entries(self):
        response = self.client.post("/api/v1/entries/", json=self.ENTRY)
        assert response.json == "Created"
        assert response.status_code == 201

        response = self.client.get("/api/v1/entries/")
        assert response.json[0]["id"] == 1
        assert len(response.json) == 1
        assert response.json[0]["name"] == self.ENTRY["name"]
        assert response.json[0]["comment"] == self.ENTRY["comment"]
        assert isinstance(parser.parse(response.json[0]["created"]), datetime.datetime)
        assert response.status_code == 200
