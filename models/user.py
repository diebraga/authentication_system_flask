from database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
