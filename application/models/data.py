from flask.ext.mongoengine import Document, EmbeddedDocument
import time

class Vector(EmbeddedDocument):
	x = FloatField(required=True)
	y = FloatField(required=True)
	z = FloatField(required=True)

class DataPoint(EmbeddedDocument):
	time = DateTimeField(required = True)
	gps = GeoPointField()
	accel = EmbeddedDocument(Vector)
	gyro = EmbeddedDocument(Vector)
	throttle = FloatField()
	brake = FloatField()

class DataSession(Document):
	driver = StringField(required = True)
	start_time = DateTimeField(required = True)
	end_time = DateTimeField()
	data = ListField(DataPoint)

# If there are no admin users create a temporary one
if DataSession.objects().count() == 0:
	data_temp = DataSession()
	# TODO : create some sample data to test on the app
	data_temp.save()