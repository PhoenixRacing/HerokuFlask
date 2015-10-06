#Model bullshit here
#Use subteams.py as a guide for how to structure this
from flask import url_for

class team_member(object):
	def __init__(self, name = "nobody", image_path= "person-placeholder.jpg", major="Engineering", year="201X",title=' ',contact=' '):
		self.name = name
		self.image_path = image_path
		self.major = major
		self.year = year
		self.title = title
		self.contact = contact

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

anders = team_member()
anders.name = "Anders Johnson"
anders.image_path = 'img/team/anders.jpg'
anders.major = 'Mechanical Engineering'
anders.year = '2017'
anders.title = 'General Project Manager'
anders.contact = 'anders.johnson@students.olin.edu'

joe = team_member()
joe.name = 'Joe Kochevar'
joe.image_path = 'img/team/joe.jpeg'
joe.major = 'Mechanical Engineering'
joe.year = '2016'
joe.title = 'Design Lead'
joe.contact = 'joseph.kochevar@students.olin.edu'

harris = team_member()
harris.name = "Harris Davidson"
harris.image_path = 'img/team/harris_davidson.jpg'
harris.major = "Mechanical Engineering"
harris.year = "2019"
harris.title = "Fabrication Manager"
harris.contact = "harris.davidson@students.olin.edu"

deborah = team_member()
deborah.name = 'Deborah Hellen'
deborah.image_path = 'img/team/deborah.jpg'
deborah.major = "Electrical and Computer Engineering"
deborah.year = '2016'
deborah.title = 'Website and Marketing Lead'
deborah.contact = 'deborah.hellen@students.olin.edu'

daniel = team_member()
daniel.name = 'Daniel Leong'
daniel.image_path = 'img/team/daniel.jpg'
daniel.major = "Mechanical Engineering"
daniel.year = '2016'
daniel.contact = 'daniel.leong@students.olin.edu'

lindsey = team_member()
lindsey.name = 'Lindsey Andrade'
lindsey.image_path = 'img/team/lindsay.JPG'
lindsey.major = 'Mechanical Engineering'
lindsey.year = '2017'
lindsey.contact = 'lindsey.andrade@students.olin.edu'

kevin = team_member()
kevin.name = 'Kevin Suzuki'
kevin.image_path = 'img/team/ksuzi.JPG'
kevin.major = 'Bioengineering'
kevin.year = '2017'
kevin.title = 'Financial Manager'
kevin.contact = 'kevin.suzuki@students.olin.edu'

brett = team_member()
brett.name = 'Brett Atkinson'
brett.image_path = 'img/team/brett.jpg'
brett.major = 'Mechanical Engineering'
brett.year = '2017'
brett.title = "Body System Lead"
brett.contact = 'brett.atkinson@students.olin.edu'

manik = team_member()
manik.name = 'Manik Singh Sethi'
manik.image_path = 'img/team/manik.jpg'
manik.major = 'Mechanical Engineering'
manik.year = '2018'
manik.title = "Drivetrain System Lead"
manik.contact = 'Manik.Sethi@students.olin.edu'

sawyer = team_member()
sawyer.name = 'Sawyer Vaughan'
sawyer.image_path = 'img/team/sawyer.jpg'
sawyer.major = 'Electrical and Computer Engineering'
sawyer.year = '2017'
sawyer.contact = 'Sawyer.vaughan@students.olin.edu'

searing = team_member()
searing.name = 'Michael Searing'
searing.image_path = 'img/team/searing.jpg'
searing.major = 'Mechanical Engineering'
searing.year = '2016'
searing.contact = 'michael.searing@students.olin.edu'

kelli = team_member()
kelli.name = "Kelli Shimazu"
kelli.image_path = 'img/team/kelli.jpg'
kelli.major = "Mechanical Engineering"
kelli.year = "2018"
kelli.contact = "kelli.shimazu@students.olin.edu"

keenan = team_member()
keenan.name = "Keenan Zucker"
keenan.image_path = 'img/team/keenan.jpg'
keenan.major = 'Mekeenanical Engineering'
keenan.year = '2018'
keenan.title = "Old Car Czar"
keenan.contact = 'keenan.zucker@students.olin.edu'

forrest = team_member()
forrest.name = "Forrest Bourke"
forrest.image_path = "img/team/forrest.jpg"
forrest.major = "Electrical and Computer Engineering"
forrest.year = '2016'
forrest.contact = "forrest.bourke@students.olin.edu"

patrick = team_member()
patrick.name = "Patrick Huston"
patrick.image_path = "img/team/patrick.jpg"
patrick.major = "Electrical and Computer Engineering"
patrick.year = "2018"
patrick.contact = "patrick.huston@students.olin.edu"

kai = team_member()
kai.name = "Kai Levy"
kai.image_path = "img/team/kai.jpg"
kai.major = "Electrikail and Computer Engineering"
kai.year = "2018"
kai.contact = "kai.levy@students.olin.edu"

michael = team_member()
michael.name = "Michael Resnick"
michael.image_path = "img/team/rezzy.jpg"
michael.major = "Mechanical Engineering"
michael.year = "2016"
michael.contact = "michael.resnick@students.olin.edu"

jc = team_member()
jc.name = "Juan Carlos del Rio"
jc.image_path = "img/team/jc.jpg"
jc.major = "Mechanical Engineering"
jc.year = "2018"
jc.contact = "juancarlos.delrio@students.olin.edu"

radmer = team_member()
radmer.name = "Radmer van der Hyde"
radmer.image_path = "img/team/radmer.jpg"
radmer.major = "Electrical and Computer Engineering"
radmer.year = "2017"
radmer.contact = "radmer.vanderhyde@students.olin.edu"


team_leads = {'joe': joe, "harris": harris, 'anders': anders}

system_leads = {'manik': manik, 'brett': brett, 'jc': jc, 'radmer': radmer}

general_mems = {'kevin': kevin, 'daniel':daniel, 'lindsey': lindsey,\
	'brett': brett, 'manik':manik, 'sawyer':sawyer, \
	'searing': searing, 'kelli':kelli, 'keenan':keenan, \
	'forrest': forrest, 'patrick': patrick, 'kai': kai,\
	"michael": michael, 'deborah': deborah}
