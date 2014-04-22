# from flask.ext.mongoengine import Document, EmbeddedDocument
from .. import db, app

class Vector(db.EmbeddedDocument):
	x = db.FloatField(required=True)
	y = db.FloatField(required=True)
	z = db.FloatField(required=True)

class DataPoint(db.EmbeddedDocument):
	time = db.DateTimeField(required = True)	#DateTime
	gps = db.GeoPointField()					#Location(gps=[<lon>,<lat>])
	accel = db.EmbeddedDocumentField(Vector)	#[<x>,<y>,<z>]
	gyro = db.EmbeddedDocumentField(Vector)		#[<x>,<y>,<z>]
	throttle = db.FloatField()					
	brake = db.FloatField()
	speed = db.FloatField()
	tach = db.FloatField()
	frontLeftWheel = db.FloatField()
	frontRightWheel = db.FloatField()
	backLeftWheel = db.FloatField()
	backRightWheel = db.FloatField()

class DataSession(db.Document):
	driver = db.StringField()
	start_time = db.DateTimeField(required = True)
	end_time = db.DateTimeField()
	data = db.ListField(db.EmbeddedDocumentField(DataPoint))

# If there are no admin users create a temporary one
if app.config['TEST']:
	from datetime import datetime, timedelta
	from random import random
	from math import sin, cos

	# Delete all previous data
	DataSession.objects().delete()

	# Create the data session
	data_temp = DataSession()
	data_temp.driver = "kush"
	data_temp.start_time = datetime.now()
	data_temp.end_time = datetime.now() + timedelta(minutes = 20)
	# Populate with 100 data points
	data_temp.data = [DataPoint(time=datetime.now() + timedelta(seconds=i),\
								gps=[sin(i/100.0),cos(i/100.0)],\
								accel=Vector(x=random(),y=random(),z=random()),\
								gyro=Vector(x=random(),y=random(),z=random()),\
								throttle=random(),\
								brake=random(),\
								speed=random(),\
								tach=random(),\
								frontLeftWheel=random(),\
								frontRightWheel=random(),\
								backLeftWheel=random(),\
								backRightWheel=random()) for i in xrange(100)]
	# Save the data session object
	data_temp.save() 	