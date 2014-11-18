from flask import url_for

class Picture(object):
	def __init__(self, name=None, image_path=None, caption=None):
		self.name = name
		self.image_path = image_path
		self.caption = caption

team_pic = Picture()
team_pic.name = "Team Picture"
team_pic.image_path = "img/2014teampic.JPG"
team_pic.caption = "The 2014 team photo"

flag = Picture()
flag.name = "baja Flag"
flag.image_path = "img/bajaflag.jpg"
flag.caption = "We have a flag and stuff"

car1 = Picture()
car1.name = "sierra"
car1.image_path = "img/twitter_maybe.jpg"
car1.caption = "the 2013 racing vehicle at competition"

picture_list = [team_pic, flag, car1]
