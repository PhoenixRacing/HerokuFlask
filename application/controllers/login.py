from flask import render_template, request, redirect, flash, url_for
from ..models.forms import LogInForm

def login():
	form = LogInForm(request.form)
	if request.method == 'POST' and form.validate():
		flash('Email: {0}\nPassword: {1}'.format(form.email.data,form.password.data))
		return redirect(url_for('index'))
	return render_template('login.html', form=form)