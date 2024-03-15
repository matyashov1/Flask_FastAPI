
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()



class Users(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.Stringr(200), nullable=False)
    password = db.Column(db.Stringr(200), nullable=False)

    def __repr__(self):
        return f'Student({self.name}, {self.last_name})'
