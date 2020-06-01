import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# mongoDB config 
app.config["MONGO_DBNAME"] = os.environ.get('HC_MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('HC_MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    # Returns the index.html and passes in all recipes from the database
    all_recipes = mongo.db.recipes.find()
    return render_template('index.html', recipes=all_recipes)


@app.route('/featured/<sortby>')
def featured_sorted(sortby):
    # Returns the featured.html and passes in featured recipes from the database
    # with a variable for some sorting options
    featured_recipes = None
    if sortby == 'a-z':
        featured_recipes = mongo.db.recipes.find({'featured': 'true'}).sort([('name', 1)])
        a_to_z = 'a-z'
    elif sortby == 'z-a':
        featured_recipes = mongo.db.recipes.find({'featured': 'true'}).sort([('name', -1)])
        a_to_z = 'z-a'
    return render_template('featured.html', recipes=featured_recipes, a_to_z=a_to_z)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
