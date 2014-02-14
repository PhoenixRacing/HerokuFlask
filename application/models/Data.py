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

if __name__ == '__main__':
	dummydata = []
	for i in range(1,100):
		datapoint = DataPoint(time=datetime.now())
		dummydata.append(DataSession(driver = 'Patrick'+str(i),start_time = time.gmtime(([1392308290+(i*10)]))))
	print str(dummydata)