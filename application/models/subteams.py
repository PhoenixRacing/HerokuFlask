from flask import url_for

class Subteam(object):
	def __init__(self, name=None, image_path=None, short_description=None, description=None):
		self.name = name
		self.image_path = image_path
		self.short_description = short_description
		self.description = description

chassis = Subteam()
chassis.name = 'chassis'
chassis.image_path = 'img/chassis-icon.png'
chassis.short_description = 'Designs our frame from 4130 chromoly steel tube and performs structural analysis.'
chassis.description = 'Body Subteam is in charge of the chassis, stylistic elements, and driver interface. Goals for this year include making the chassis smaller and making sure that everyone on the team can drive the car safely and comfortably.\nThis year will be the third year in a row that the team is building an entirely new car, which opens up many opportunities for redesign and testing. Some examples of redesign for this year include making the car smaller overall to cut down weight and increase maneuverability and handling, to take a look at different types of bracing to make sure the car can handle significant impacts, and to ensure that all members of the team can drive the car safely and in accordance with the SAE technical rules. We learned a lot while designing the chassis last year and will include elements such as ease of manufacturing that were vital to building the last car.\nUsing FEA (Finite Element Analysis) we are able to simulate impacts on the car to insure driver safety. Building sketch models around drivers help visualize designs and improve driver interface. These and other techniques are combined with SolidWorks CAD to design a car to meet our goals.\nBuilding the chassis is not possible without the help of the Olin Machine Shop where team members are trained to use a variety of techniques and machines to help put the car together. We are able to use tools like the water jet cutter and CNC router to insure that parts are made with precision.'

drivetrain = Subteam()
drivetrain.name = 'drivetrain'
drivetrain.image_path = 'img/drivetrain-icon.png'
drivetrain.short_description = 'Designs and fabricates our gearbox around an adapted differential and tunes our CVT.'
drivetrain.description = 'Drivetrain is responsible for everything from the engine output shaft to the gearbox input, and our job is to manage the transfer of power from the engine to the wheels. Beginning with desired overarching performance characteristics, we design, select, adapt, and tune drivetrain compoents that enable the car to perform at desired specifications. This may involve vendor parts or parts we design and fabricate ourselves. \n Last year, we used a team-designed two-stage chain reduction, housed in billet aluminum machined in-house at Olin College, along with atunable CVT (continuously variable transmission.) This year, we plan on redesigning our drivetrain from the ground up, including a single-level, size-reduced drivetrain, as well as a new CVT and new differential. Our design changes will be focused primarily on optimizing our car\'s center of gravity and making our drivetrain more robust in order to endure longer races with fewer, more easily-serviceable features.'

electrical = Subteam()
electrical.name = 'electrical'
electrical.image_path = 'img/electrical-icon.png'
electrical.short_description = 'Performs real-time performance analysis on the car and maintains the website.'
electrical.description = 'Electrical is the newest Phoenix Racing subsystem. We\'re responsible for everything from wiring the car\'s brake lights, to tracking car speed, to maintaining the team website.\n This year we will be focusing on creating and running simulations to validate the designs for the car\'s drivetrain, body, and suspension systems. We will also be equipping the car with a sensor suite to allow us to conduct real-time failure analysis on the car and to provide the driver with useful data during races and practice drives. Lastly, we will be implementing a reliable driver communication system to help the driver more effectively communicate with teammembers in the pit and on the sidelines.'

suspension = Subteam()
suspension.name = 'suspension'
suspension.image_path = 'img/suspension-icon.png'
suspension.short_description = 'Performs geometric optimization for maximum handling and cornering performance.'
suspension.description = 'Suspension seeks to optimize the car\'s handling and ensure that it can tackle as many of the competition obstacles as possible. Before designing parts, we create complex geometric sketches taht predict the roll axis, camber, toe, Ackerman, and steering radius of the car. From these sketches we design the suspension to be durable and replaceable to weather the difficult obstacles taht the car faces. \n This year, we want to further decrease the car\'s turning radius, correct some handling issues, do more comprehensive analysis on the loads that the suspension system is subjected to, and perfect our adjustable shock mount design. The adjustable shock mount is an Olin original idea that allows us to even out the handling characteristics for drivers of all weights.'

subteam_list = {'chassis':chassis, 'drivetrain':drivetrain, 'electrical':electrical, 'suspension':suspension}