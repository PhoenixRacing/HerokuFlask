from flask import request, jsonify
import os
from werkzeug.utils import secure_filename
from .. import app, allowed_file

def upload():
	file = request.files['file']
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return jsonify(filename=filename, url=url_for('uploaded_file',filename=filename))