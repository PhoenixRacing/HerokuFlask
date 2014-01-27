from flask import render_template
from ..models.forms import SignUpForm

def signup():
	return render_template('signup.html')