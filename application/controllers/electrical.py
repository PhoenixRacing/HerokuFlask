from flask import request, render_template

title = "Electrical"
text = "Electrical subteam is just two years old. We do everything from wiring the brake lights to getting feedback to the driver. We haven't encountered any other SAE Baja teams pushing the boundaries of what an electrical subteam could do, and we're excited to find out.\nThis year, we're equipping the car with a speedometer, tachometer, and a dashboard that will give drivers information such as speed, race stats, and gas level. We are also working on a driver communications system that would let the driver talk to the pit captain during races."

def electrical():
	return render_template('subteamdescription.html',title=title,text=text.split('\n'))