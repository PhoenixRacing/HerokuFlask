from flask import url_for, abort, render_template, g
from flask.ext.login import LoginManager, login_required, fresh_login_required, current_user
# from flask.ext.cors import cross_domain
from . import app, login_manager
import controllers
from functools import wraps

def admin_required(f):
	@wraps(f)
	def wrapper(*args,**kwargs):
		if not current_user.is_admin():
			return abort(401)
		return f(*args,**kwargs)
	return wrapper

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_name='Page Not Found', error_description='found a page that doesn\'t exist'), 404

@app.errorhandler(401)
def page_not_found(e):
    return render_template('error.html', error_name='Permission Denied', error_description='tried to access a page under false pretenses'), 404

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

@app.route("/user/edit_password/", methods=['GET','POST'])
@fresh_login_required
def edit_password():
	return "edit password\nthis page needs to be created"

@app.route("/admin/", methods=['GET','POST'])
@fresh_login_required
@admin_required
def admin_page():
	return controllers.admin_page()


@app.route("/admin/modify_access/<user_id>/", methods=['POST'])
@login_required
@admin_required
def modify_access(user_id):
	return controllers.modify_access(user_id)

@app.route("/admin/delete/<user_id>/", methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
	return controllers.delete_user(user_id)

@app.route("/blog/")
def blog():
	return controllers.blog()