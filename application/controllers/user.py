from flask import render_template, request, redirect, url_for
from flask.ext.login import current_user
from ..models import EditUserForm

def user():
	return render_template('user.html')#,user=current_user)

def edit_user():
	form = EditUserForm(request.form)
	if request.method == 'POST' and form.validate():
		if len(form.data['first_name']) > 0:
			current_user.first_name = form.data['first_name']
		if len(form.data['last_name']) > 0:
			current_user.last_name = form.data['last_name']
		if len(form.data['email']) > 0:
			current_user.email = form.data['email']
		current_user.save()
		return redirect(url_for('user'))


	return render_template('edit_user.html', form=form)