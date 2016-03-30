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

anders = team_member()
anders.name = "Anders Johnson"
anders.image_path = 'img/team/Johnson_Anders.jpg'
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
keenan.major = 'Human Centered Computing'
keenan.year = '2018'
keenan.title = "Old Car Czar"
keenan.contact = 'keenan.zucker@students.olin.edu'

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

jc = team_member()
jc.name = "Juan Carlos del Rio"
jc.image_path = "img/team/jc.jpg"
jc.major = "Mechanical Engineering"
jc.title = "Suspension Lead"
jc.year = "2018"
jc.contact = "juancarlos.delrio@students.olin.edu"

radmer = team_member()
radmer.name = "Redmer van der Heyde"
radmer.image_path = "img/team/radmer.jpg"
radmer.major = "Electrical and Computer Engineering"
radmer.title = "Electrical Lead"
radmer.year = "2017"
radmer.contact = "radmer.vanderhyde@students.olin.edu"

keving = team_member()
keving.name = "Kevin Guo"
keving.image_path = "img/team/kevin_guo.jpg"
keving.year = "2019"
keving.major = "Undeclared"
keving.contact = "kevin.guo@students.olin.edu"

andrew = team_member()
andrew.name = "Andrew Holmes"
andrew.image_path = "img/team/Holmes_Andrew.jpg"
andrew.year = "2019"
andrew.major = "Mechanical Engineering"
andrew.contact = "andrew.holmes@students.olin.edu"

andrewp = team_member()
andrewp.name = "Andrew Pan"
andrewp.image_path = "img/team/andrew_pan-1.jpg"
andrewp.year = "2019"
andrewp.major = "Undeclared"
andrewp.contact = "andrew.pan@students.olin.edu"

hunter = team_member()
hunter.name = "Hunter Normandeau"
hunter.image_path = "img/team/hunter_normandeau-1.jpg"
hunter.year = "2019"
hunter.major = "Mechanical Engineering"
hunter.contact = "hunter.Normandeau@students.olin.edu"

gwyn = team_member()
gwyn.name = "Gwyn Phelps"
gwyn.image_path = "img/team/gwyn_phelps-2.jpg"
gwyn.year = "2019"
gwyn.major = "Undeclared"
gwyn.contact = "gwyn.phelps@students.olin.edu"

mary = team_member()
mary.name = "Mary Keenan"
mary.image_path = "img/team/mary_keenan-2.jpg"
mary.major = "Undeclared"
mary.contact = "mary.keenan@students.olin.edu"

uma = team_member()
uma.name = "Uma Desai"
uma.image_path = "img/team/uma_desai-1.jpg"
uma.major = "Undeclared"
uma.contact = "uma.desai@students.olin.edu"

steven = team_member()
steven.name = "Steven Meyer"
steven.image_path = "img/team/steven_meyer-2.jpg"
steven.major = "Mechanical Engineering"
steven.contact = "steven.meyer@students.olin.edu"

team_leads = {'joe': joe, "harris": harris, 'anders': anders}

system_leads = {'manik': manik, 'brett': brett, 'jc': jc, 'radmer': radmer}

general_mems = {'kevin': kevin, 'daniel':daniel, 'lindsey': lindsey,\
	'sawyer':sawyer, 'hunter':hunter, 'gwyn':gwyn, 'mary':mary, 'uma':uma,\
	'searing': searing, 'kelli':kelli, 'keenan':keenan, 'steven':steven,\
	'kai': kai,'keving': keving, 'andrew': andrew, 'andrewp': andrewp,\
	'deborah': deborah}
