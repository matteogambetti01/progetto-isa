from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def homepage():
    return render_template("base.html")

@home.route('/searchByTitle')
def searchByTitle():
    return "<h1> RICERCA PER TITOLO </h1>"

@home.route('/searchByDate')
def searchByDate():
    return "<h1> RICERCA PER DATA  </h1>"