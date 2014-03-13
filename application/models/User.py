from flask.ext.mongoengine import Document
from flask.ext.mongoengine.wtf import model_form
from .. import db, login_manager, flask_bcrypt

access = ('admin','edit','none')

class User(db.Document):
	first_name = db.StringField(max_length=50, required=True)
	last_name = db.StringField(max_length=50, required=True)
	email = db.EmailField(required=True)
	password = db.StringField(required=True)
	access = db.StringField(default='none', required=True)
	
	def __init__(self, *args, **kwargs):
		# catch the form keyword
		if 'form' in kwargs:
			super(User,self).__init__()
			# build User from form object
			data = kwargs['form'].data
			self.first_name = data['first_name']
			self.last_name = data['last_name']
			self.email = data['email']
			self.password = flask_bcrypt.generate_password_hash(data['password'])
			self.access = 'none'
		else:
			super(User,self).__init__(*args,**kwargs)

	def is_admin(self):
		return self.access == 'admin'

	def can_edit(self):
		return self.access in ['admin','edit']	

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def check_password(self,password):
		return flask_bcrypt.check_password_hash(self.password,password)

	def __eq__(self, other):
		if isinstance(other, User):
			return self.get_id() == other.get_id()
		return False

	def __ne__(self, other):
		return not self.__eq__(other)

# If there are no admin users create a temporary one
if User.objects(access='admin').count() == 0:
	admin_temp = User()
	admin_temp.first_name = 'Phoenix'
	admin_temp.last_name = 'Racing'
	admin_temp.email = 'phoenix.racing@baja.olin.edu'
	admin_temp.password = flask_bcrypt.generate_password_hash('The_Phoenix_Flies')
	admin_temp.access = 'admin'
	admin_temp.save()

@login_manager.user_loader
def load_user(email):
	user_query = User.objects(email = email)
	if user_query.count() > 0:
		return user_query.first()
	else:
		return None