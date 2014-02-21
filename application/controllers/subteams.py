from flask import request, render_template

def subteams():
	return render_template('subteams.html', active_page='subteams')