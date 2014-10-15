from wtforms import Form, TextField, TextAreaField, PasswordField, validators

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

class BlogPostForm(Form):
	title = TextField('Title', [validators.DataRequired()])
	body = TextAreaField('Body', [validators.DataRequired()])

class EditPasswordForm(Form):
	old_password = PasswordField('Old Password', [validators.Required()])
	new_password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm_new_password', message='Passwords must match')])
	confirm_new_password = PasswordField('Confirm New Password', [validators.Required(), validators.EqualTo('new_password', message='Passwords must match')])

class PurchaseForm(Form):
	name = TextField('Name', [validators.DataRequired(), validators.Length(min=3,max=30)])
	item = TextField('Item', [validators.DataRequired(), validators.Length(min=3,max=30)])
	cost = TextField('Cost', [validators.DataRequired()])
	vendor = TextField('Vendor', [validators.DataRequired()])
	link = TextField('Link', [validators.Length(min=3,max=30), validators.URL(require_tld=True, message=u'Invalid link.')])
	date = TextField('Date Needed', [validators.DataRequired()])
	quantity = TextField('Quantity', [validators.DataRequired()])

