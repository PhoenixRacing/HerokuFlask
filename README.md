PhoenixRacingWebApp#noregrets
===========
A web app for the Olin College MiniBaja team.

First Time Use
---------------
Install the Heroku toolbelt. For Ubuntu this command is:
```
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```
The setup script included is intended to run on Ubuntu. To change permissions and execute the script run:
```
source setup.sh
```
If you are working on a different operating system, or if you would rather setup manually you will need to:
- Setup a Python virtualenv
- Install all of the dependencies in requirements.txt in the virtualenv

Install MongoDB
--------------
Install MongoDB on Ubuntu:
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10;
echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" | sudo tee /etc/apt/sources.list.d/10gen.list;
sudo apt-get update;
sudo apt-get install mongodb-10gen;
```

Repeated Use
--------------
This package uses a Python virtualenv to manage dependencies. This means that each time you want to run your app locally you must first load the virtualenv. To do this simply run the command:
```
source venv/bin/activate
```
If you start adding dependencies to the project you will need to add them to the requirements.txt file. The easiest way to do this is to load the virtualenv and run the command
```
pip freeze > requirements.txt
```
in your virtualenv. This dumps all of the currently installed package information into requirements.txt.

Deploying to Heroku
------------------
Once you are ready to deploy your app to Heroku for the first time, you must first create a Heroku account. To create a Heroku account visit the Heroku [quickstart guide](https://devcenter.heroku.com/articles/quickstart). Once you have an account and you have installed the Heroku client you can create your app from the command line using the command:
```
heroku create <your-app-name>
```
From then on you can push your changes to the Heroku server with the command
```
git push heroku master
```

For more information regarding Python and Heroku you can visit the [Getting Started guide](https://devcenter.heroku.com/articles/getting-started-with-python).