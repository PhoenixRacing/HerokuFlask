#Model bullshit here
#Use subteams.py as a guide for how to structure this
from flask import url_for

class team_member(object):
	def __init__(self, name = "nobody", image_path= "img/some_bullshit.jpg", bio="Ya I don't have one"):
		self.name = name
		self.image_path = image_path
		self.bio = bio

# Maybe a way to reduce the amount of information we need to input??

# team_member_object_list = []
# team_member_name_list = ['Kate','Chris','Debora']
# team_member_image_path_list = ['','','']
# team_member_bio_list = ['','','']
# for i in range(len(team_member_name_list)):
# 	member_object = team_member()
# 	member_object.name = team_member_name_list[i]
# 	member_object.image_path = team_member_image_path_list[i]
# 	member_object.bio = team_member_bio_list[i]
# 	team_member_object_list.append(member_object)

# for i in team_member_object_list
# 	team_list = {i.name:i}

kate = team_member()
kate.name = 'Kate'
# kate.image_path = ''
# kate.bio = ''

chris = team_member()
chris.name = 'Chris'

maddie = team_member()
maddie.name = 'Maddie'


team_list = {'Kate':kate, 'Chris':chris, 'Maddie':maddie}
