from flask import render_template
from ..models import BlogPost

def blog():
	return render_template('blog.html',posts=BlogPost.objects())