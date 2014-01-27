#!/bin/bash
gksudo pip install virtualenv
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt