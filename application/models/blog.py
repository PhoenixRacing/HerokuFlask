from .. import db

class BlogPost(db.Document):
	title = db.StringField(required=True)
	body = db.StringField(required=True)
	# TODO - include reference to the User that created the post
	# TODO - include a timestamp for the creation of the post

	@property
	def p_list(self):
	    return self.body.split('\n')

if BlogPost.objects().count() < 1:
	post = BlogPost()
	post.title = "Test Post"
	post.body = "This is the body of the post. This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.\nThis is the body of the post.This is the body of the post.This is the body of the post.\nThis is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post.This is the body of the post."
	post.save()