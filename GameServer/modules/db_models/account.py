from modules.models import db
from flask_login import UserMixin

class Account(UserMixin, db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f"<Account {self.username}>"
