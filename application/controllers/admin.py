from flask import render_template, redirect, url_for, request, flash, abort, json
from ..models import User

def admin_page():
	users = User.objects()
	return render_template('admin.html',users=users)

def delete_user(user_id):
	user = User.objects(id=user_id).first()
	if user.access == "admin" and User.objects(access="admin").count() <= 1:
		return json.jsonify({"error":"You cannot delete the last admin"}), 409
	User.objects(id=user_id).delete()
	return redirect(url_for('admin_page'))

def modify_access(user_id):
	new_access = request.json['access']
	if new_access not in User.access_levels:
		return json.jsonify({"error":"Bad Request"}), 400

	user = User.objects(id=user_id)

	if user.count() <= 0:
		return json.jsonify({"error":"Bad User ID"}), 409

	user = user.first()

	if user.access == "admin" and User.objects(access="admin").count() <= 1:
		return json.jsonify({"error":"You cannot remove the last admin"}), 409

	user.access = new_access
	user.save()
	return 200
