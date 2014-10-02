from flask import request, render_template
from flask.ext.login import current_user
from ..models import team_list

def team():
	return render_template('team.html', active_page='team', team_members = team_list.values())

