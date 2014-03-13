from flask import render_template, request, redirect, flash, url_for
from flask.ext.login import login_user
from ..models.forms import SignUpForm
from ..models.User import User

def signup():
	form = SignUpForm(request.form)
	if request.method == 'POST' and form.validate():
		# Check for users with the same email
		if len(User.objects(email = form.data['email'])) > 0:
			redirect(url_for('login'))
		else:
			new_user = User(form = form)
			print new_user
			new_user.save()
			login_user(new_user)
			return redirect(url_for('index'))
		# Create the user object
	return render_template('signup.html', form=form, active_page='signup')