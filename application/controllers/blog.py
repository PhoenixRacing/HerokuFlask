from flask import render_template, request, redirect, url_for
from ..models import BlogPost, BlogPostForm

from wtforms import Form, TextField, TextAreaField, PasswordField, validators
from .. import app

def view_blog():
	return render_template('blog.html',posts=BlogPost.objects())

def view_post(post_id):
	post = BlogPost.objects(id=post_id).first()
	return render_template('blog_post.html',post=post)


def create_post():
	post = BlogPost()
	form = BlogPostForm(request.form)
	if request.method == 'POST' and form.validate():
		post.title = form.data['title']
		post.body = form.data['body']
		post.save()
		return redirect(url_for('view_blog'))
	return render_template('edit_post.html',form=form)

def edit_post(post_id):
	post = BlogPost.objects(id=post_id).first()
	form = BlogPostForm(request.form, post)

	print form
	if request.method == 'POST':
		data = request.form['body'].split('<h2>')[1].split('</h2>')
		post.title = data[0]
		post.body = data[1]
		post.save()
		return redirect(url_for('view_blog'))
		
	return render_template('edit_post.html', form=form, post=post)

def delete_post(post_id):
	post = BlogPost.objects(id=post_id).first()
	post.delete()

	return redirect(url_for('view_blog'))