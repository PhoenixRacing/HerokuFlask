from . import app
import controllers

@app.route("/")
@app.route("/index/")
def index():
	return controllers.index()

@app.route("/login/", methods=['GET', 'POST'])
def login():
	return controllers.login()

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
	return controllers.signup()

@app.route("/subteams/")
def subteams():
	return controllers.subteams()