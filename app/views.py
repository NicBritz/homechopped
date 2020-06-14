from app import app
from app.setup import MONGO, DB_RECIPES
from flask import render_template, redirect, url_for, request
import random


##############
# INDEX VIEW #
##############
@app.route('/', defaults={'pg': 1, 'limit': 8, 'sort': 1})
@app.route('/<pg>/<limit>/<sort>')
def index(pg, limit, sort):
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

    # sorting
    if int(sort) == 1:
        sort = 1
    else:
        sort = -1

    # pagination
    limit = int(limit)
    skip = 0 if int(pg) == 1 else (int(pg) - 1) * limit
    paginated_recipes = DB_RECIPES.find().sort([('name', sort)]).skip(skip).limit(limit)

    return render_template('index.html', all_recipes=all_recipes, paginated_recipes=paginated_recipes,
                           random_recipes=random_recipes, limit=limit, current_pg=pg, sort=sort)


######################
# INDEX LIMIT AMOUNT #
######################
@app.route('/index_limit/', methods=['POST'])
def index_limit():
    """Changes the number of recipes per page
        :param
        number selected
        :return
        index with number per page
    """
    amount = int(request.form.get('amount'))
    return redirect(url_for('index', pg=1, limit=amount, sort=1, _anchor='recipe-list'))


##############
# INDEX SORT #
##############
@app.route('/index_sort/<pg>/<limit>/', methods=['POST'])
def index_sort(pg, limit):
    """Sorts recipes on the index page
        :param
        number selected
        :return
        index with number per page
    """
    sort = int(request.form.get('sort'))

    return redirect(url_for('index', pg=pg, limit=limit, sort=sort, _anchor='recipe-list'))


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
