from ..db import ActiveModel, db

class Entry(ActiveModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    body = db.Column(db.String(255), unique=True)

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Entry %r>' % self.title

