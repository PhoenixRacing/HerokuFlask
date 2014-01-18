from flask import Flask
import router
import controllers

app = Flask(__name__)
app.debug = True

@app.route("/")
@app.route("/index")
def index():
	print "hello"
	return controllers.index()
