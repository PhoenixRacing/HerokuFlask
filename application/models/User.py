from .. import db

class User(db.Document):
	name = db.StringField(max_length=50, required=True)