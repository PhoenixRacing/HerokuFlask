from flask.ext.mongoengine import Document
from .. import db

access = ('admin','edit','none')

class User(db.Document):
	first_name = db.StringField(max_length=50, required=True)
	last_name = db.StringField(max_length=50, required=True)
	access = db.StringField(default = 'none', required=True)