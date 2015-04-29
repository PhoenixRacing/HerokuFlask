from flask import url_for
from os import listdir
from os.path import isfile, join

class Picture(object):
	def __init__(self, image_path=None, caption=""):
		self.image_path = image_path
		self.caption = caption


anders_enduro = Picture()
anders_enduro.image_path = "img/gallery/andersenduro.jpg"
anders_enduro.caption = ""

anders_enduro2 = Picture()
anders_enduro2.image_path = "img/gallery/andersendurostart.jpg"
anders_enduro2.caption = ""

anders_in_car = Picture()
anders_in_car.image_path = "img/gallery/andersincar.jpg"
anders_in_car.caption = ""

car_driving = Picture()
car_driving.image_path = "img/gallery/cardriving.jpg"
car_driving.caption = ""

car_driving2 = Picture()
car_driving2.image_path = "img/gallery/cardriving2.jpg"
car_driving2.caption = ""

deborah_car = Picture()
deborah_car.image_path = "img/gallery/deborahcar.jpg"
deborah_car.caption = ""

joe_grinding = Picture()
joe_grinding.image_path = "img/gallery/joegrinding.jpg"
joe_grinding.caption = ""

juan_numbers = Picture()
juan_numbers.image_path = "img/gallery/juannumbers.jpg"
juan_numbers.caption = ""

teampic2013 = Picture()
teampic2013.image_path = "img/gallery/2013teampic.jpg"
teampic2013.caption = "The 2012-2013 Phoenix Racing team picture"

tenn_competition = Picture()
tenn_competition.image_path = "img/gallery/tune-up-tenn.JPG"
tenn_competition.caption = "Preparing the car for the dynamic events at the 2013 Tennessee competition"

tenn_enduro = Picture()
tenn_enduro.image_path = "img/gallery/enduro-tenn.JPG"
tenn_enduro.caption = "The car on the rock crawl during the endurance race in Tennessee"

tenn_strat = Picture()
tenn_strat.image_path = "img/gallery/enduro-strategy-tenn.JPG"
tenn_strat.caption = "Tim and Ert discuss race strategy during a pit stop."

rochester2013 = Picture()
rochester2013.image_path = "img/gallery/rochester2013.jpg"
rochester2013.caption = "The team at the 2013 Baja SAE Competition in Rochester, NY"

rochestermud = Picture()
rochestermud.image_path = "img/gallery/rochester_mud.jpg"
rochestermud.caption = "Racing in the mud at the 2013 Rochester, NY competition"

rochestermud2 = Picture()
rochestermud2.image_path = "img/gallery/more_mud.jpg"
rochestermud2.caption = "The muddy endurance race at the Rochester competition"

rochestermud3 = Picture()
rochestermud3.image_path = "img/gallery/even_more_mud.jpg"
rochestermud3.caption = "More mud in Rochester, NY"

driveday = Picture()
driveday.image_path = "img/gallery/driveday2013.jpg"
driveday.caption = "Drive day! Practicing on our track at home"

teampic2014 = Picture()
teampic2014.image_path = "img/gallery/2014teampic.jpg"
teampic2014.caption = "The 2013-3014 Phoenix Racing team picture"

chassis2014 = Picture()
chassis2014.image_path = "img/gallery/chassis.JPG"
chassis2014.caption = "Finally finished welding the chassis for the 2014 competition car!"

chris_chassis = Picture()
chris_chassis.image_path = "img/gallery/chris_with_chassis.JPG"
chris_chassis.caption = "Chris with the completed chassis"

chassis_work = Picture()
chassis_work.image_path = "img/gallery/chassis_work.JPG"
chassis_work.caption = "Assembling the 2014 competition car"

suspension = Picture()
suspension.image_path = "img/gallery/suspension.JPG"
suspension.caption = "Daniel assembling the suspension system"

workday = Picture()
workday.image_path = "img/gallery/workday.JPG"
workday.caption = "Maddie, Kate, and Kevin during a work day"

elpaso_waiting = Picture()
elpaso_waiting.image_path = "img/gallery/enduro-el-paso.JPG"
elpaso_waiting.caption = "Eerik waiting for the endurance race to begin"

dust_elpaso = Picture()
dust_elpaso.image_path = "img/gallery/dust-el-paso.JPG"
dust_elpaso.caption = "Lindsey and Rezzy improvise dust protection gear in El Paso."

elpaso_team = Picture()
elpaso_team.image_path = "img/gallery/el-paso-team.JPG"
elpaso_team.caption = "The team after the El Paso endurance race"

enduro_elpaso = Picture()
enduro_elpaso.image_path = "img/gallery/enduro_elpaso.jpg"
enduro_elpaso.caption = "Eerik and the car after the endurance race in El Paso, TX"

hill_climb = Picture()
hill_climb.image_path = "img/gallery/hill-climb.JPG"
hill_climb.caption = "The hill climb in El Paso"

pit_kansas = Picture()
pit_kansas.image_path = "img/gallery/pit-kansas.JPG"
pit_kansas.caption = "Preparing the pit for the competition in Pittsburg, Kansas"

kansas_tech = Picture()
kansas_tech.image_path = "img/gallery/kansas-passed-tech.JPG"
kansas_tech.caption = "First team to pass tech inspection at the 2014 Kansas Competition!"

maddie_kevin = Picture()
maddie_kevin.image_path = "img/gallery/maddie_kevin.JPG"
maddie_kevin.caption = "Maddie and Kevin after the acceleration race in Kansas"

kansas_enduro = Picture()
kansas_enduro.image_path = "img/gallery/kansas_enduro.JPG"
kansas_enduro.caption = "The endurance race during the 2014 Baja Competition in Pittsburg, Kansas"


picture_list = [anders_enduro2, anders_enduro, anders_in_car, car_driving, car_driving2, \
	deborah_car, joe_grinding, juan_numbers ,teampic2013, tenn_competition, tenn_strat, \
	tenn_enduro, rochestermud, rochestermud2, rochestermud3, rochester2013, driveday, \
	teampic2014, chassis2014, chris_chassis, chassis_work, workday, suspension, \
	elpaso_waiting, dust_elpaso, hill_climb, enduro_elpaso, elpaso_team, pit_kansas, \
	kansas_tech, maddie_kevin, kansas_enduro]


#TODO: support admin uploads to the gallery page