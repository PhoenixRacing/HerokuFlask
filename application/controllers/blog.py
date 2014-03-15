from flask import render_template
from ..models import BlogPost

def blog():
	return render_template('blog.html',posts=BlogPost.objects())

def create_blog():
	return "This page needs to be created"

def edit_blog():
	return "This page needs to be created"