from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

# Setup the app object
app = Flask(__name__)
app.debug = True

# Setup BCrypt
flask_bcrypt = Bcrypt(app)

# Setup the Database
app.config.from_pyfile('mongo_config.cfg')
db = MongoEngine(app)

# Setup the log in system
login_manager = LoginManager()
login_manager.init_app(app)

# The router cannot run until the app and database are created
import router