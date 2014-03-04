from flask import request, render_template

title = "Suspension"
text = "Suspension makes sure that the car handles as well as it possibly can. Through optimizing the roll axis, camber, and other parameters, we make sure that the car performs optimally on all kinds of terrain for all drivers, not just on asphalt for 150-lb drivers. Despite being one of the longest cars at the competition (56 inch track length), Olin has one of the smallest turning radii at 7 feet.\nThis year, we want to further reduce our bump steer, further tune our shocks for optimal performance across the entire camber curve, and update our adjustable shock mount design: an Olin original idea that allows us to even out the handling characteristics for drivers of all weights."

def suspension():
	return render_template('subteamdescription.html',title=title,text=text.split('\n'))