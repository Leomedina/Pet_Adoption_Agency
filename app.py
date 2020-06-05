from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import *
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "KEY_IS_A_SECRET"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

@app.route("/")
def show_home():
    return render_template("home.html")