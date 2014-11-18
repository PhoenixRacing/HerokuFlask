from flask import request, render_template
from ..models import picture_list
from flask.ext.login import current_user

def gallery():
	return render_template('gallery.html', active_page='gallery',pictures=picture_list)