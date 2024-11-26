from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Account(UserMixin, db.Model):
    __tablename__ = 'accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    joined = db.Column(db.DateTime, server_default=db.func.now())
    last_login = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<Account {self.username}>"
