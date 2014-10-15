#!/bin/bash
gksudo pip install virtualenv
virtualenv venv --distribute
source venv/bin/activate
sudo apt-get install python-dev
pip install -r requirements.txt