from flask import render_template
from flask.ext.login import current_user

def sponsors():
	return render_template('sponsors-temp.html', active_page='sponsors')
