from flask import render_template, request, redirect, url_for
from ..models import BlogPost, BlogPostForm

def blog():
	return render_template('blog.html',posts=BlogPost.objects())

def create_blog():
	post = BlogPost()
	form = BlogPostForm(request.form)
	if request.method == 'POST' and form.validate():
		post.title = form.data['title']
		post.body = form.data['body']
		post.save()
		return redirect(url_for('blog'))
	return render_template('edit_blog.html',form=form)

def edit_blog(post_id):
	post = BlogPost.objects(id=post_id).first()
	form = BlogPostForm(request.form)
	if request.method == 'POST' and form.validate():
		post.title = form.data['title']
		post.body = form.data['body']
		post.save()
		return redirect(url_for('blog'))
		# edit the post and save it
	return render_template('edit_blog.html', form=form, post=post)