from flask import url_for
from os import listdir
from os.path import isfile, join

class Picture(object):
	def __init__(self, image_path=None, caption=""):
		self.image_path = image_path
		self.caption = caption

teampic2013 = Picture()
teampic2013.image_path = "img/gallery/2013teampic.jpg"
teampic2013.caption = "The 2012-2013 Phoenix Racing team picture."

rochester2013 = Picture()
rochester2013.image_path = "img/gallery/rochester2013.jpg"
rochester2013.caption = "The team at the 2013 Baja SAE Competition in Rochester, NY."

rochestermud = Picture()
rochestermud.image_path = "img/gallery/rochester_mud.jpg"
rochestermud.caption = "Racing in the mud at the 2013 Rochester NY competition."

rochestermud2 = Picture()
rochestermud2.image_path = "img/gallery/more_mud.jpg"
rochestermud2.caption = "The muddy endurance race at the Rochester competition."

rochestermud3 = Picture()
rochestermud3.image_path = "img/gallery/even_more_mud.jpg"

driveday = Picture()
driveday.image_path = "img/gallery/driveday2013.jpg"
driveday.caption = "Drive day! Practicing on our track at home."

teampic2014 = Picture()
teampic2014.image_path = "img/gallery/2014teampic.jpg"
teampic2014.caption = "The 2013-3014 Phoenix Racing team picture."

chassis2014 = Picture()
chassis2014.image_path = "img/gallery/chassis.JPG"
chassis2014.caption = "Finally finished welding the chassis for the 2014 competition car!"

chris_chassis = Picture()
chris_chassis.image_path = "img/gallery/chris_with_chassis.JPG"
chris_chassis.caption = "Chris with the completed chassis"

chassis_work = Picture()
chassis_work.image_path = "img/gallery/chassis_work.JPG"
chassis_work.caption = "Assembling the 2014 competition car."

suspension = Picture()
suspension.image_path = "img/gallery/suspension.JPG"
suspension.caption = "Daniel assembling the suspension system."

enduro_elpaso = Picture()
enduro_elpaso.image_path = "img/gallery/enduro_elpaso.jpg"
enduro_elpaso.caption = "After the endurance race at the 2014 Baja SAE Competition in El Paso, TX."

kansas_enduro = Picture()
kansas_enduro.image_path = "img/gallery/kansas_enduro.JPG"
kansas_enduro.caption = "The endurance race during the 2014 Baja SAE Competition in Pittsburg, Kansas."


picture_list = [teampic2013, rochester2013, rochestermud, rochestermud2, \
	rochestermud3, driveday, teampic2014, chassis2014, chris_chassis, \
	chassis_work, suspension, enduro_elpaso, kansas_enduro]


#TODO: support admin uploads to the gallery page