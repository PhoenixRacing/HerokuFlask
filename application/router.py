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

@app.route("/data/", methods=['GET','POST'])
def data():
	return controllers.data()

@app.route("/subteams/")
def subteams():
	return controllers.subteams()

@app.route("/donate/")
def donate():
	return controllers.donate()

@app.route("/sponsors/")
def sponsors():
	return controllers.sponsors()

@app.route("/chassis/")
def chassis():
	return controllers.chassis()

@app.route("/drivetrain/")
def drivetrain():
	return controllers.drivetrain()

@app.route("/suspension/")
def suspension():
	return controllers.suspension()

@app.route("/electrical/")
def electrical():
	return controllers.electrical()