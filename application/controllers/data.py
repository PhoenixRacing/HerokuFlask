from flask import request, render_template
from flask.ext.login import current_user
from ..models import DataSession

def data():
	first_data = DataSession.objects().first()
	speed = [data.speed for data in first_data.data]
	tach = [data.tach for data in first_data.data]
	return render_template('data.html', active_page='data', speed = speed, tach = tach)