from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ActiveModel(object):
    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
