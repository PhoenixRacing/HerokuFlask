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

kate = team_member()
kate.name = 'Kate Maschan'
kate.image_path = 'img/team/kate.jpg'
kate.major = 'Mechanical Engineering'
kate.year = '2015'
kate.title = 'General Project Manager'
kate.contact = 'kate@students.olin.edu'

chris = team_member()
chris.name = "Chris Joyce"
chris.image_path = 'img/team/chris.jpg'
chris.major = 'Mechanical Engineering'
chris.year = '2015'
chris.title = 'Design Lead'
chris.contact = 'christopher.Joyce@students.olin.edu'

maddie = team_member()
maddie.name = "Maddie Perry"
maddie.image_path = 'img/team/maddie.jpg'
maddie.major = 'Mechanical Engineering'
maddie.year = '2015'
maddie.title = 'Fabrication Manager'
maddie.contact = 'madeline.perry@students.olin.edu'

joe = team_member()
joe.name = 'Joe Kochevar'
joe.image_path = 'img/team/joe.jpeg'
joe.major = 'Mechanical Engineering'
joe.year = '2016'
joe.title = 'Drivetrain System Lead'
joe.contact = 'joseph.kochevar@students.olin.edu'

deborah = team_member()
deborah.name = 'Deborah Hellen'
deborah.image_path = 'img/team/deborah.jpg'
deborah.major = "Electrical and Computer Engineering"
deborah.year = '2016'
deborah.title = 'Electrical System Lead'
deborah.contact = 'deborah.hellen@students.olin.edu'

daniel = team_member()
daniel.name = 'Daniel Leong'
daniel.image_path = 'img/team/daniel.jpg'
daniel.major = "Mechanical Engineering"
daniel.year = '2016'
daniel.title = 'Suspension System Lead'
daniel.contact = 'daniel.leong@students.olin.edu'

lindsey = team_member()
lindsey.name = 'Lindsey Andrade'
lindsey.image_path = 'img/team/lindsay.JPG'
lindsey.major = 'Mechanical Engineering'
lindsey.year = '2017'
lindsey.title = 'Body System Lead'
lindsey.contact = 'lindsey.andrade@students.olin.edu'

kevin = team_member()
kevin.name = 'Kevin Suzuki'
kevin.image_path = 'img/team/ksuzi.JPG'
kevin.major = 'Bioengineering'
kevin.year = '2017'
kevin.title = 'Financial Manager'
kevin.contact = 'kevin.suzuki@students.olin.edu'

brandon = team_member()
brandon.name = 'Brandon Chiou'
brandon.image_path = 'img/team/brandon.jpg'
brandon.major = 'Bioengineering'
brandon.year = '2016'
brandon.contact = 'brandon.chiou@students.olin.edu'

anders = team_member()
anders.name = "Anders Johnson"
anders.image_path = 'img/team/anders.jpg'
anders.major = 'Mechanical Engineering'
anders.year = '2017'
anders.contact = 'anders.johnson@students.olin.edu'

meg = team_member()
meg.name = 'Meg McCauley'
meg.image_path = 'img/team/meg.jpg'
meg.major = 'Electrical and Computer Engineering'
meg.year = '2017'
meg.contact = 'meg@students.olin.edu'


selina = team_member()
selina.name = "Ziyu (Selina) Wang"
selina.image_path = 'img/team/selina.JPG'
selina.major = 'Electrical and Computer Engineering'
selina.year = '2018'
selina.contact = 'ziyu.wang@students.olin.edu'

brett = team_member()
brett.name = 'Brett Atkinson'
brett.image_path = 'img/team/brett.jpg'
brett.major = 'Mechanical Engineering'
brett.year = '2017'
brett.contact = 'brett.atkinson@students.olin.edu'

manik = team_member()
manik.name = 'Manik Singh Sethi'
manik.image_path = 'img/team/manik.jpg'
manik.major = 'Mechanical Engineering'
manik.year = '2018'
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
keenan.contact = 'keenan.zucker@students.olin.edu'

zoe = team_member()
zoe.name = "Zoe Fiddler"
zoe.image_path = 'img/team/zoe.jpg'
zoe.major = "Electrical and Computer Engineering"
zoe.year = '2016'
zoe.contact = 'zoe.fiddler@students.olin.edu'

ad = team_member()
ad.name = "Adriana Garties"
ad.image_path = 'img/team/Ad_headshot.jpg'
ad.major = "Mechanical Engineering"
ad.year = '2015'
ad.contact = 'ad@students.olin.edu'

lauren = team_member()
lauren.name= 'Lauren Froschauer'
lauren.image_path = 'img/team/lauren.jpg'
lauren.major = 'Mechanical Engineering'
lauren.year = '2016'
lauren.contact = 'LaurenFroschauer@gmail.com'

luke = team_member()
luke.name = "Luke Morris"
luke.image_path = "img/team/luke.jpg"
luke.major = 'Mechanical Engineering'
luke.year = '2017'
luke.contact = "luke.morris@students.olin.edu"

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
kai.major = "Electrical and Computer Engineering"
kai.year = "2018"
kai.contact = "kai.levy@students.olin.edu"

michael = team_member()
michael.name = "Michael Resnick"
michael.image_path = "img/team/rezzy.jpg"
michael.major = "Mechanical Engineering"
michael.year = "2016"
michael.contact = "michael.resnick@students.olin.edu"

emily = team_member()
emily.name = "Emily Guthrie"
emily.image_path = "img/team/emily.jpg"
emily.major = "Electrical and Computer Engineering"
emily.year = "2016"
emily.contact = "emily.guthrie@students.olin.edu"


team_leads = {'chris': chris, 'maddie': maddie, 'kate': kate}

system_leads = {'joe': joe, 'deborah': deborah, 'daniel': daniel, 'lindsey': lindsey}

general_mems = {'kevin': kevin, 'brandon': brandon, 'anders': anders, \
	'selina': selina, 'brett': brett, 'manik':manik, 'sawyer':sawyer, \
	'searing': searing, 'kelli':kelli, 'keenan':keenan, 'zoe': zoe, 'ad': ad, \
	'lauren': lauren, 'luke': luke, 'forrest': forrest, 'patrick': patrick, 'kai': kai,\
	"michael": michael, 'meg': meg, 'emily': emily}
