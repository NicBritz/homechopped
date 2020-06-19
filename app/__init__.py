from flask import Flask

# Create app instance
app = Flask(__name__)

# Reference:
# https://pythonise.com/series/learning-flask/flask-application-structure

#####################
# MAIN DEPENDENCIES #
#####################
from app import setup
from app import views
from app import login
from app import profile
from app import recipe
from app import errors
