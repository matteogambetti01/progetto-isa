from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from app.routes.auth import auth
from app.routes.post import post
from app.routes.comment import comment
from app.routes.home import home

# defining database
db = SQLAlchemy()
DB_NAME = "forum.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Creating blueprints
    app.register_blueprint(post, url_prefix='/post')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(comment, url_prefix='/comment')
    app.register_blueprint(home, url_prefix='/')

    return app