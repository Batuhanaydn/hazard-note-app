from . import *
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataNote = db.Column(db.String(65535), unique=True)
    datetime = db.Column(db.Date(), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(256), unique=True)
    firstname = db.Column(db.String(256), unique=False)
    password = db.Column(db.String(256), unique=False)
    tel = db.Column(db.String(256), unique=True)
    notes = db.relationship('Note')
