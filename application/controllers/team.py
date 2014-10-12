from flask import request, render_template
from flask.ext.login import current_user
from ..models import team_leads, general_mems, system_leads

def team():
	return render_template('team.html', active_page='team', \
	general_members = general_mems.values(), team_leads=team_leads.values(), system_leads=system_leads.values())

