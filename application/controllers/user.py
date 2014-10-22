from flask import render_template, request, redirect, url_for
from flask.ext.login import current_user
from ..models import EditUserForm, EditPasswordForm, Notify, ForgotPasswordForm
from ..models import User
import string
import random

def user():
	if request.args.get('notify'):
		notification = Notify()
		notification.type = request.args.get('notify_type')
		notification.message = request.args.get('notify_message')
	else:
		notification = None
	return render_template('user.html', notify=notification)

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

def forgot_password():
	form = ForgotPasswordForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User.objects(email = form.data['email'])
		if user.count() > 0:
			old_user = user.first()
			new_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
			old_user.password = new_password
			old_user.save()
			send_email(form.data['email'], new_password)
			#send_email('sawyer.vaughan@students.olin.edu', new_password)
			notification = Notify(notification_type = 'success', message = 'Check your email')
			return redirect(url_for('edit_password', notify = True, notify_type = notification.type, notify_message = notification.message))
	return render_template('forgot_password.html', form=form)

def edit_password():
	form = EditPasswordForm(request.form)
	if request.method == 'POST' and form.validate():
		if current_user.check_password(form.data['old_password']):
			print(current_user.check_password(form.data['old_password']))
			current_user.password = form.data['new_password'];
			current_user.save()
			notification = Notify(notification_type = 'success', message = 'Successfully Changed Password')
			return redirect(url_for('user', notify = True, notify_type = notification.type, notify_message = notification.message))
		else:
			notification = Notify(notification_type = 'error', message = 'Old Password Incorrect') 
			return render_template('edit_password.html', form=form, notify = notification)
	return render_template('edit_password.html', form=form)

def send_email(email, new_password):
    import smtplib
 
    gmail_user = "recover.phoenixracing@gmail.com"
    gmail_pwd = "PhoenixRacing"
    FROM = 'recover.phoenixracing@gmail.com'
    TO = [email] #must be a list
    SUBJECT = "Reset Your Password"
    TEXT = "You requested a new password for olinbaja.com. Your new password for olinbaja.com is "+new_password+". Please login to olinbaja.com as soon as possible to change your password to something you will remember."

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
    except:
        print "failed to send mail"
