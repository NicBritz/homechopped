from flask import Flask

# Create app instance
app = Flask(__name__)

# import dependencies
from app import setup
from app import user_login
from app import app_main
from app import user_profile
from app import errors

