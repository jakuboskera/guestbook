from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class EntriesModel(db.Model):
    __tablename__ = "entries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    comment = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment
        self.created = datetime.utcnow()
