import flask, os
from flask import Flask, url_for
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager, current_user
from flask.ext.bcrypt import Bcrypt
from flask.ext.socketio import SocketIO, emit
from functools import wraps
from gevent import monkey

# Setup the app object
monkey.patch_all()

app = Flask(__name__)

# Setup BCrypt
flask_bcrypt = Bcrypt(app)

# Setup the Database
host = os.environ.get('MONGODB_HOST')
if host:
    app.config['MONGODB_HOST'] = host
    app.config['MONGODB_PORT'] = os.environ.get('MONGODB_PORT')
    app.config['MONGODB_DB'] = os.environ.get('MONGODB_DB')
    app.config['MONGODB_USERNAME'] = os.environ.get('MONGODB_USERNAME')
    app.config['MONGODB_PASSWORD'] = os.environ.get('MONGODB_PASSWORD')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['TEST'] = False
else:
    app.config.from_pyfile('mongo_config.cfg')
    app.config['TEST'] = True

socketio = SocketIO(app)
db = MongoEngine(app)

# Setup the login system
login_manager = LoginManager()
login_manager.init_app(app)

# Setup File Uploads
# UPLOAD_FOLDER = '/static/uploads/'
UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Setup globals in the views
def render_decorator(f):
    @wraps(f)
    def dec(*args,**kwargs):
        # always add the current user to the view
        return f(*args,user=current_user,**kwargs)
    return dec

flask.render_template = render_decorator(flask.render_template)

# The router cannot run until the app and database are created
import router


if __name__ == "__main__":
    socketio.run(app)