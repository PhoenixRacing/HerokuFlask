from flask.ext.mongoengine import Document, EmbeddedDocument

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
	start_time = DateTimeField(required = True)
	end_time = DateTimeField()
	data = ListField(DataPoint)