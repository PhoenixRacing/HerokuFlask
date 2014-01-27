from wtforms import Form, TextField, PasswordField, validators

class LogInForm(Form):
	email = TextField('Email',[validators.Required(), validators.Length(min=6,max=50)])
	password = PasswordField('Password',[validators.Required()])

class SignUpForm(Form):
	name = TextField('Full Name', [validators.Length(min=4, max=50)])
	email = TextField('Email', [validators.Required(), validators.Length(min=6,max=50)])
	password = PasswordField('Password', [validators.Required(), validators.EqualTo('confirmPassword',message='Passwords must match')])
	confirmPassword = PasswordField('Repeat Password')