from flask import request, render_template
from ..models import subteam_list
from flask.ext.login import current_user

def subteams():
	sub_list = subteam_list.values()
	sub_list.sort()
	return render_template('subteams.html', active_page='subteams',subteams=sub_list)

def description(team):
	return render_template('subteamdescription.html', team=subteam_list[team], text=subteam_list[team].description.split('\n'))