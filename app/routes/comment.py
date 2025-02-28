from flask import Blueprint

comment = Blueprint('comment', __name__)

@comment.route('/add/<id_post>')
def add_comment():
    pass

@comment.route('/delete/<id>')
def delete_comment():
    pass

@comment.route('/update/<id>')
def update_comment():
    pass