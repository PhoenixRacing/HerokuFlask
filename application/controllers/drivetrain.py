from flask import request, render_template

title = "Drivetrain"
text = "Drivetrain Subteam is responsible for everything from the output of the engine to the input to the wheels and our job is to manage the transfer of power from the engine to the wheels. Beginning with the performance specifications the team would like to have on a given car, we design and select drivetrain components that will enable the car to perform at the desired specifications. This may involve vendor parts or parts we design and fabricate ourselves.\n Currently, we use a team-designed 2-stage reduction chain drive housed in billet aluminium machined in-house at Olin College. This year, we plan to focus on conducting detailed research studies on key parts of the drivetrain and examine the design decisions that we made. We also plan on making changes to parts where we found areas to improve over the course of the past year. All this is in an effort to continuously improve upon efficiency and performance of the drivetrain for years to come."

def drivetrain():
	return render_template('subteamdescription.html',title=title,text=text.split('\n'))