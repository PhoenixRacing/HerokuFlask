from flask import request, render_template

def index():
	return render_template('index.html', active_page='index')