from flask import render_template

def sponsors():
	return render_template('sponsors.html', active_page='sponsors')