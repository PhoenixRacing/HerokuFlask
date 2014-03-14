from wtforms import Form, TextField, PasswordField, validators

class LogInForm(Form):
	email = TextField('Email',[validators.Required(), validators.Length(min=6,max=50)])
	password = PasswordField('Password',[validators.Required()])

class SignUpForm(Form):
	first_name = TextField('First Name', [validators.Length(min=2, max=50), validators.DataRequired()])
	last_name = TextField('Last Name', [validators.Length(min=2, max=50), validators.DataRequired()])
	email = TextField('Email', [validators.DataRequired(), validators.Email()])
	password = PasswordField('Password', [validators.Required(), validators.EqualTo('confirm_password',message='Passwords must match')])
	confirm_password = PasswordField('Repeat Password')

class EditUserForm(Form):
	first_name = TextField('First Name', [validators.Length(min=2, max=50), validators.DataRequired()])
	last_name = TextField('Last Name', [validators.Length(min=2, max=50), validators.DataRequired()])
	email = TextField('Email', [validators.DataRequired(), validators.Email()])

class EditPasswordForm(Form):
	old_password = PasswordField('Old Password', [validators.Required()])
	new_password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm_new_password', message='Passwords must match')])
	confirm_new_password = PasswordField('Confirm New Password', [validators.Required(), validators.EqualTo('new_password', message='Passwords must match')])