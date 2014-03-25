from flask import request, render_template
from ..models import subteam_titles, subteam_descriptions
from flask.ext.login import current_user

def subteams():
	return render_template('subteams.html', active_page='subteams')

def description(team):
	return render_template('subteamdescription.html', title=subteam_titles[team], text=subteam_descriptions[team].split('\n'))