from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# User table definition
class User(db.Model, UserMixin):
    username = db.Column(db.String(250), primary_key=True)
    email = db.column(db.String(200), unique=True)
    password = db.column(db.String(50))
    isAdmin = db.column(db.Boolean, default=False)
    # Defining relationships
    comments = db.relationship('Comment')
    posts = db.relationship('Post')

# Post table definition
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now()) 
    user_id = db.Column(db.String(250), db.ForeignKey('user.username')) # Foreign key

# Comment table definition
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now()) 
    user_id = db.Column(db.String(250), db.ForeignKey('user.username')) # Foreign key