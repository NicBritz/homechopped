from app import app
from flask import render_template
from app.setup import MONGO


@app.route('/')
def index():
    # Returns the index.html and passes in all recipes from the database
    #
    all_recipes = MONGO.db.recipes.find()
    return render_template('index.html', recipes=all_recipes)
