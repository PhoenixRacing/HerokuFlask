# donate.py

from flask import render_template

def donate():
	return render_template('donate.html', active_page='donate')