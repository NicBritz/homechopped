from app import app
from app.setup import MONGO, DB_RECIPES
from flask import render_template


##############
# INDEX VIEW #
##############
@app.route('/')
def index():
    """ Renders the index view
    :return
    index.html from the render templates directory passing in all the recipes from the recipe database
    """
    return render_template('index.html', all_recipes=DB_RECIPES.find())


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
