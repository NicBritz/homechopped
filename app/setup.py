from app import app
import cloudinary as cloudinary
import os
from flask_pymongo import PyMongo

# cloudinary config
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

# mongoDB config
app.config["MONGO_DBNAME"] = os.environ.get('HC_MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('HC_MONGO_URI')

# secret key
app.config["SECRET_KEY"] = os.environ.get('SESSION_SECRET')

# constant variables
MONGO = PyMongo(app)
DB_RECIPES = MONGO.db.recipes
DB_USERS = MONGO.db.users