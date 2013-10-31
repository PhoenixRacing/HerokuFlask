HerokuFlask
===========

The skeleton for a Flask app that is designed to run on Heroku. This skeleton employs the MVC architecture and serves only test content.

Dependencies
--------------
Python 2.7 (suggested version)
Virtualenv:
'''
sudo pip install virtualenv
'''

First Time Use
---------------
Designed to run on Ubuntu, you set everything up by running the setup.sh script.

To make the script executable run:
'''
chmod +x setup.sh
'''

To execute the script in your current session run:
'''
source setup.sh
'''

Repeated Use
--------------
This package uses a Python virtualenv to manage dependencies. This means that each time you want to run your app locally you must first load the virtualenv.

To do this simply run the command:
'''
source venv/bin/activate
'''

Python virtualenv
---------------
This skeleton takes advantage of a Python virtualenv, which is generally a good idea as it helps manage dependencies and prevents your application from breaking as you update dependencies. The downside of using the virtualenv is that, to ensure you are using the right dependencies, you must load the virtualenv each time you open a new terminal. This command is:
'''
source venv/bin/activate
'''

As your app grows it will probably take on more dependencies. As you do this, you must update your requirements.txt file, so that Heroku will also use the appropriate dependencies. To do this you must load the virtualenv and type the command:
'''
pip freeze -l > requirements.txt
'''