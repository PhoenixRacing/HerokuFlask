from flask import render_template, redirect, url_for, request
from ..models import User

def admin_page():
	users = User.objects()
	return render_template('admin.html',users=users)

def delete_user(user_id):
	User.objects(id=user_id).delete()
	return redirect(url_for('admin_page'))

def modify_access(user_id):
	new_access = request.json['access']
	# raise Exception(str(new_access))
	# return new_access
	if new_access in User.access_levels:
		user = User.objects(id=user_id)
		if user.count() > 0:
			user = user.first()
			user.access = new_access
			user.save()
	return redirect(url_for('admin_page'))