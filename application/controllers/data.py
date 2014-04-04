from flask import request, render_template
from flask.ext.login import current_user
from ..models import DataSession

def data():
	first_data = DataSession.objects().first()
	return render_template('data.html', active_page='data', data_session=first_data)