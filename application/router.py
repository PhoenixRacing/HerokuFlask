from flask import url_for
from flask.ext.login import LoginManager, login_required, fresh_login_required
from . import app, login_manager
import controllers

@app.route("/")
@app.route("/index/")
def index():
	return controllers.index()

@app.route("/login/", methods=['GET', 'POST'])
def login():
	return controllers.login()

login_manager.login_view = 'login'

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
	return controllers.signup()

# @login_required
@app.route("/logout/",methods=['GET','POST'])
def logout():
	return controllers.logout()

@app.route("/data/", methods=['GET','POST'])
def data():
	return controllers.data()

@app.route("/subteams/")
def subteams():
	return controllers.subteams()

@app.route("/subteams/<subteam_name>/")
def subteam_description(subteam_name):
	return controllers.description(subteam_name)

@app.route("/donate/")
def donate():
	return controllers.donate()

@app.route("/sponsors/")
def sponsors():
	return controllers.sponsors()

@app.route("/chassis/")
def chassis():
	return controllers.description('chassis')

@app.route("/drivetrain/")
def drivetrain():
	return controllers.description('drivetrain')

@app.route("/suspension/")
def suspension():
	return controllers.description('suspension')

@app.route("/electrical/")
def electrical():
	return controllers.description('electrical')

@app.route("/user/")
@login_required
def user():
	return controllers.user()

@app.route("/user/edit/", methods=['GET','POST'])
@fresh_login_required
def edit_user():
	return controllers.edit_user()

@app.route("/user/edit_password/",methods=['GET','POST'])
@fresh_login_required
def edit_password():
	return "edit password\nthis page needs to be created"

@app.route("/admin/",methods=['GET','POST'])
@fresh_login_required
def admin_page():
	return "admin page\nthis page needs to be created"