from flask import request, render_template
from flask.ext.login import current_user

def index():
	return render_template('index.html', active_page='index')