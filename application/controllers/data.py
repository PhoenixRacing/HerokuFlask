from flask import request, render_template, json
from flask.ext.login import current_user
from ..models import DataSession

def data():
	if DataSession.objects().count() > 0:
		first_data = DataSession.objects().first()
		return render_template('data.html', active_page='data', data=first_data.to_json())
	else:
		return render_template('data.html', active_page='data', data=None)