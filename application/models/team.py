#Model bullshit here
#Use subteams.py as a guide for how to structure this
from flask import url_for

class team_member(object):
	def __init__(self, name = "nobody", image_path= "person-placeholder.jpg", major="Engineering", year="20XX",title=' ',contact=' '):
		self.name = name
		self.image_path = image_path
		self.major = major
		self.year = year
		self.title = title
		self.contact = contact

team_leads = {}
system_leads = {}
general_mems = {}

anders = team_member()
anders.name = "Anders Johnson"
anders.image_path = 'img/team/Johnson_Anders.jpg'
anders.major = 'Mechanical Engineering'
anders.year = '2017'
anders.title = 'Project Manager'
anders.contact = 'anders.johnson@students.olin.edu'
team_leads['anders'] = anders

harris = team_member()
harris.name = "Harris Davidson"
harris.image_path = 'img/team/harris_davidson.jpg'
harris.major = "Mechanical Engineering"
harris.year = "2017"
harris.title = "Product Owner"
harris.contact = "harris.davidson@students.olin.edu"
team_leads['harris'] = harris

lindsey = team_member()
lindsey.name = 'Lindsey Andrade'
lindsey.image_path = 'img/team/lindsey.jpg'
lindsey.major = 'Mechanical Engineering'
lindsey.year = '2017'
lindsey.title = 'Design and Fabrication Manager'
lindsey.contact = 'lindsey.andrade@students.olin.edu'
team_leads['lindsey'] = lindsey

manik = team_member()
manik.name = 'Manik Singh Sethi'
manik.image_path = 'img/team/manik_sethi.png'
manik.major = 'Mechanical Engineering'
manik.year = '2018'
manik.title = "Drivetrain Lead"
manik.contact = 'Manik.Sethi@students.olin.edu'
system_leads['manik'] = manik

jc = team_member()
jc.name = "Juan Carlos del Rio"
jc.image_path = "img/team/jc.jpg"
jc.major = "Mechanical Engineering"
jc.title = "Suspension Lead"
jc.year = "2018"
jc.contact = "juancarlos.delrio@students.olin.edu"
system_leads['jc'] = jc

radmer = team_member()
radmer.name = "Radmer van der Heyde"
radmer.image_path = "img/team/radmer.jpg"
radmer.major = "Electrical and Computer Engineering"
radmer.title = "Electrical Lead"
radmer.year = "2017"
radmer.contact = "radmer.vanderhyde@students.olin.edu"
system_leads['radmer'] = radmer

sawyer = team_member()
sawyer.name = 'Sawyer Vaughan'
sawyer.image_path = 'img/team/sawyer.jpg'
sawyer.major = 'Electrical and Computer Engineering'
sawyer.year = '2017'
sawyer.title = 'Software Lead'
sawyer.contact = 'Sawyer.vaughan@students.olin.edu'
system_leads['sawyer'] = sawyer

kevin = team_member()
kevin.name = 'Kevin Suzuki'
kevin.image_path = 'img/team/ksuzi.JPG'
kevin.major = 'Bioengineering'
kevin.year = '2017'
kevin.title = 'Financial Manager'
kevin.contact = 'kevin.suzuki@students.olin.edu'
general_mems['kevin'] = kevin

mary = team_member()
mary.name = "Mary Keenan"
mary.image_path = "img/team/mary_keenan.jpg"
mary.major = "Electrical and Computer Engineering"
mary.year = '2019'
mary.contact = "mary.keenan@students.olin.edu"
general_mems['mary'] = mary

keenan = team_member()
keenan.name = "Keenan Zucker"
keenan.image_path = 'img/team/keenan_zucker.jpg'
keenan.major = 'Human Centered Computing'
keenan.year = '2018'
keenan.contact = 'keenan.zucker@students.olin.edu'
general_mems['keenan'] = keenan

kai = team_member()
kai.name = "Kai Levy"
kai.image_path = "img/team/kai.jpg"
kai.major = "Electrikail and Computer Engineering"
kai.year = "2018"
kai.contact = "kai.levy@students.olin.edu"
general_mems['kai'] = kai

gwyn = team_member()
gwyn.name = "Gwyn Phelps"
gwyn.image_path = "img/team/gwyn_phelps-2.jpg"
gwyn.year = "2019"
gwyn.major = "Undeclared"
gwyn.contact = "gwyn.phelps@students.olin.edu"
general_mems['gwyn'] = gwyn

andrew = team_member()
andrew.name = "Andrew Holmes"
andrew.image_path = "img/team/Holmes_Andrew.jpg"
andrew.year = "2019"
andrew.major = "Mechanical Engineering"
andrew.contact = "andrew.holmes@students.olin.edu"
general_mems['andrew'] = andrew

andrewp = team_member()
andrewp.name = "Andrew Pan"
andrewp.image_path = "img/team/andrew_pan-1.jpg"
andrewp.year = "2019"
andrewp.major = "Engineering with Computing"
andrewp.contact = "andrew.pan@students.olin.edu"
general_mems['andrewp'] = andrewp

hunter = team_member()
hunter.name = "Hunter Normandeau"
hunter.image_path = "img/team/hunter_normandeau-1.jpg"
hunter.year = "2019"
hunter.major = "Mechanical Engineering"
hunter.contact = "hunter.Normandeau@students.olin.edu"
general_mems['hunter'] = hunter

uma = team_member()
uma.name = "Uma Desai"
uma.image_path = "img/team/uma_desai-1.jpg"
uma.major = "Electrical and Computer Engineering"
uma.year = '2019'
uma.contact = "uma.desai@students.olin.edu"
general_mems['uma'] = uma

steven = team_member()
steven.name = "Steven Meyer"
steven.image_path = "img/team/steven_meyer-2.jpg"
steven.major = "Mechanical Engineering"
steven.year = '2019'
steven.contact = "steven.meyer@students.olin.edu"
general_mems['steven'] = steven

evan = team_member()
evan.name = "Evan Cusato"
evan.image_path = "img/team/evan_cusato.jpg"
evan.major = "Mechanical Engineering"
evan.year = '2020'
evan.contact = "evan.cusato@students.olin.edu"
general_mems['evan'] = evan

miranda = team_member()
miranda.name = "Miranda Lao"
miranda.image_path = "img/team/miranda_lao.jpg"
miranda.major = "Undeclared"
miranda.year = '2020'
miranda.contact = "miranda.lao@students.olin.edu"
general_mems['miranda'] = miranda

missoury = team_member()
missoury.name = "Missoury Lytle"
missoury.image_path = "img/team/missoury_lytle.jpg"
missoury.major = "Chemical Engineering"
missoury.year = '2020'
missoury.contact = "missoury@students.olin.edu"
general_mems['missoury'] = missoury

adam = team_member()
adam.name = "Adam Selker"
adam.image_path = "img/team/adam_selker.jpg"
adam.major = "Undeclared"
adam.year = '2020'
adam.contact = "adam@students.olin.edu"
general_mems['adam'] = adam

benjamin = team_member()
benjamin.name = "Benjamin Lilly"
benjamin.image_path = "img/team/benjamin_lilly.jpg"
benjamin.major = "Mechanical Engineering"
benjamin.year = '2020'
benjamin.contact = "benjamin.lilly@students.olin.edu"
general_mems['benjamin'] = benjamin

elena = team_member()
elena.name = "Elena Meyerson"
elena.image_path = "img/team/elena_meyerson.JPG"
elena.major = "Electrical and Computer Engineering"
elena.year = '2020'
elena.contact = "elena.meyerson@students.olin.edu"
general_mems['elena'] = elena

ilya = team_member()
ilya.name = "Ilya Besancon"
ilya.image_path = "img/team/ilya_besancon.jpg"
ilya.major = "Mechanical Engineering"
ilya.year = '2020'
ilya.contact = "ilya.besancon@students.olin.edu"
general_mems['ilya'] = ilya

cant_use_min_because_its_a_python_keyword = team_member()
cant_use_min_because_its_a_python_keyword.name = "Min Jang"
cant_use_min_because_its_a_python_keyword.image_path = "img/team/person-placeholder.jpg"
cant_use_min_because_its_a_python_keyword.major = "Mechanical Engineering"
cant_use_min_because_its_a_python_keyword.year = '2019'
cant_use_min_because_its_a_python_keyword.contact = "sumin.jang@students.olin.edu"
general_mems['min'] = cant_use_min_because_its_a_python_keyword

anupama = team_member()
anupama.name = "Anupama (Ana) Krishnan"
anupama.image_path = "img/team/anupama_krishnan.jpg"
anupama.major = "Mechanical Engineering"
anupama.year = '2020'
anupama.contact = "anupama.krishnan@students.olin.edu"
general_mems['anupama'] = anupama

halley = team_member()
halley.name = "Halley Pollock-Muskin"
halley.image_path = "img/team/Halley_Pollock-Muskin.jpg"
halley.major = "Mechanical Engineering"
halley.year = '2017'
halley.contact = "halley.pollock-muskin@students.olin.edu"
general_mems['halley'] = halley

anil = team_member()
anil.name = "Anil Patel"
anil.image_path = "img/team/anil_patel.jpg"
anil.major = "Undecided"
anil.year = '2017'
anil.contact = "halley.pollock-muskin@students.olin.edu"
general_mems['anil'] = anil

remy = team_member()
remy.name = "Remy Boudousquie"
remy.image_path = "img/team/remy_boudousquie.jpg"
remy.major = "Mechanical Engineering"
remy.year = '2020'
remy.contact = "remy@students.olin.edu"
general_mems['remy'] = remy






