# from flask.ext.mongoengine import Document, EmbeddedDocument
from datetime import datetime, timedelta
from .. import db, app
import time

class Vector(db.EmbeddedDocument):
	x = db.FloatField(required=True)
	y = db.FloatField(required=True)
	z = db.FloatField(required=True)

class DataPoint(db.EmbeddedDocument):
	time = db.DateTimeField(required = True)
	gps = db.GeoPointField()
	accel = db.EmbeddedDocumentField(Vector)
	gyro = db.EmbeddedDocumentField(Vector)
	throttle = db.FloatField()
	brake = db.FloatField()

class DataSession(db.Document):
	driver = db.StringField(required = True)
	start_time = db.DateTimeField(required = True)
	end_time = db.DateTimeField()
	data = db.ListField(DataPoint)

# If there are no admin users create a temporary one
if app.config['TEST']:
	DataSession.objects().delete()
	data_temp = DataSession()
	# TODO : create some sample data to test on the app
	data_temp.driver = "fuuuyes"
	data_temp.start_time = datetime.now()
	d = timedelta(minutes = 20)
	data_temp.end_time = datetime.now() + d

	data_temp.save()