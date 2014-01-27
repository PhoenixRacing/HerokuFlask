from . import app
import controllers

@app.route("/")
@app.route("/index/")
def index():
	return controllers.index()

@app.route("/login/")
def login():
	return controllers.login()

@app.route("/signup/")
def signup():
	return controllers.signup()