from datetime import datetime

from app.models import Entries


class TestModels:
    def test_new_entry(self):
        """
        GIVEN a Entries model
        WHEN a new Entry is created
        THEN check the name, comment, and date of creation
        """
        entry = Entries("Anonymous", "Guestbook is awesome!")
        assert entry.name == "Anonymous"
        assert entry.comment == "Guestbook is awesome!"
        assert isinstance(entry.created, datetime)
