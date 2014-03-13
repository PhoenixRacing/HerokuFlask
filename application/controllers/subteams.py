from flask import request, render_template
from ..models import subteam_titles, subteam_descriptions
from flask.ext.login import current_user

def subteams():
	return render_template('subteams.html', active_page='subteams', user='current_user')

def description(team):
	return render_template('subteamdescription.html', user=current_user, title=subteam_titles[team], text=subteam_descriptions[team].split('\n'))