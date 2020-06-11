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
from app import user_login
from app import user_profile
from app import recipe
from app import errors
