from app import app
from app.setup import MONGO, DB_RECIPES
from flask import render_template
import random


##############
# INDEX VIEW #
##############
@app.route('/')
def index():
    """ Renders the index view
    :return
    index.html from the render templates directory passing in all the recipes from the recipe database
    random recipes are generated for the feature slider
    """
    # all recipes
    all_recipes = DB_RECIPES.find()
    # all featured recipes
    featured_recipe_list = list(DB_RECIPES.find({'featured': 'true'}))
    # randomly select 4 from the featured
    random_recipes = random.choices(featured_recipe_list, k=4)

    return render_template('index.html', all_recipes=all_recipes, random_recipes=random_recipes)


#################
# FEATURED VIEW #
#################
@app.route('/featured/<sortby>')
def featured_sorted(sortby):
    """Renders the featured view
        :param
        a-z : sort alphabetically a-z
        z-a : sort alphabetically z-a
        :return
        featured.html with optional sort params
    """
    if sortby == 'z-a':
        featured_recipes = MONGO.db.recipes.find({'featured': 'true'}).sort([('name', -1)])
        a_to_z = 'z-a'
    else:
        featured_recipes = MONGO.db.recipes.find({'featured': 'true'}).sort([('name', 1)])
        a_to_z = 'a-z'

    return render_template('featured.html', recipes=featured_recipes, a_to_z=a_to_z)
