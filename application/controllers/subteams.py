from flask import request, render_template
from ..models import subteam_list
from flask.ext.login import current_user

def subteams():
	return render_template('subteams-temp.html', active_page='subteams',subteams=subteam_list.values())

def description(team):
	return render_template('subteamdescription.html', team=subteam_list[team], text=subteam_list[team].description.split('\n'))