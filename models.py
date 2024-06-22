from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UsersDatabase(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    fullname = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, username, fullname, age, gender, email):
        self.username = username
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'age': self.age,
            'gender': self.gender,
            'email': self.email
        }

    def __repr__(self):
        return f"{self.fullname}:{self.username}"
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UsersDatabase(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    fullname = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, username, fullname, age, gender, email):
        self.username = username
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'age': self.age,
            'gender': self.gender,
            'email': self.email
        }

    def __repr__(self):
        return f"{self.fullname}:{self.username}"
