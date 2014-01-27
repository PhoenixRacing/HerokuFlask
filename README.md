HerokuFlask
===========
The skeleton for a Flask app that is designed to run on Heroku. This skeleton employs the MVC architecture and serves only test content.

Dependencies
--------------
- Python 2.7 (suggested version)
- Virtualenv:
```
sudo pip install virtualenv
```

First Time Use
---------------
The setup script included is intended to run on Ubuntu. To change permissions and execute the script run:
```
chmod +x setup.sh
source setup.sh
```

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

Python virtualenv
---------------
This skeleton takes advantage of a Python virtualenv, which is generally a good idea as it helps manage dependencies and prevents your application from breaking as you update dependencies. The downside of using the virtualenv is that, to ensure you are using the right dependencies, you must load the virtualenv each time you open a new terminal. This command is:
```
source venv/bin/activate
```

As your app grows it will probably take on more dependencies. As you do this, you must update your requirements.txt file, so that Heroku will also use the appropriate dependencies. To do this you must load the virtualenv and type the command:
```
pip freeze -l > requirements.txt
```
