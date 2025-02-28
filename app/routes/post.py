from flask import Blueprint

post = Blueprint('views', __name__)

@post.route('/add')
def add_post():
    pass

@post.route('/delete/<id>')
def delete_post():
    pass

@post.route('/update/<id>')
def update_post():
    pass
