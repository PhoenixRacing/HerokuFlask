from .. import db

class BlogPost(db.Document):
	title = db.StringField(required=True)
	body = db.StringField(required=True)
	# TODO - include reference to the User that created the post
	# TODO - include a timestamp for the creation of the post

	def preview(self):
		# TODO - make this a preview of the blog post
		return self.body