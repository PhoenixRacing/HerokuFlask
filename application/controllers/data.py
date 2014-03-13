from flask import request, render_template
from flask.ext.login import current_user

def data():
	return render_template('data.html', active_page='data', user=current_user)