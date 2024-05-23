from app import db


class User(db.Model):
    # classe qui définit l'utilisateur
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
