from flask import redirect, url_for
from flask.ext.login import logout_user, current_user
from ..models import User

def logout():
	logout_user()
	return redirect(url_for('index'))