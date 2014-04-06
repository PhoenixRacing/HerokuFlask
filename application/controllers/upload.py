from flask import request, jsonify, url_for
import os
from werkzeug.utils import secure_filename
from .. import app, allowed_file

def upload():
	f = request.files['file']
	if f and allowed_file(f.filename):
		filename = secure_filename(f.filename)
		filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		with open(os.path.join('./application/static/uploads', filename), 'wb') as new_file:
			f.save(new_file)
		f.close()