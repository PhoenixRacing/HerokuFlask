from flask import Flask
from flask.ext.mongoengine import MongoEngine

# Setup the app object
app = Flask(__name__)
app.debug = True

# Setup the Database
app.config.from_pyfile('mongo_config.cfg')
db = MongoEngine(app)

# The router cannot work until the app and database are created
import router