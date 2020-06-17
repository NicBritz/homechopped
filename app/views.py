from app import app
from app.setup import MONGO, DB_RECIPES
from flask import render_template, redirect, url_for, request, abort
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
    # all recipes count
    all_count = DB_RECIPES.count_documents({})
    # all featured recipes
    featured_recipe_list = list(DB_RECIPES.find({'featured': 'true'}))

    count = 0

    # Error handling
    try:
        # limits user to a valid limit range
        limit = int(limit)
        if limit > all_count or limit < 2:
            # raises a 404 error if fail
            abort(404, description="Resource not found")

        # calculate the last page
        for r_page in range(all_count):
            if r_page % limit == 0:
                count += 1
        # limits user to a valid page range
        page = int(pg)
        if page > count or page < 1:
            # raises a 404 error if fail
            abort(404, description="Resource not found")
        # sorting
        sort = int(sort)
        if sort not in [1, 2]:
            # raises a 404 error if fail
            abort(404, description="Resource not found")
        if sort == 2:
            sort = -1

    except:
        # raises a 404 error if any of these fail
        abort(404, description="Resource not found")

    # randomly select 4 from the featured
    random_recipes = random.sample(featured_recipe_list, k=4)

    # pagination
    skip = 0 if int(pg) == 1 else (int(pg) - 1) * limit
    paginated_recipes = DB_RECIPES.find().sort([('name', sort)]).skip(skip).limit(limit)

    return render_template('index.html', all_recipes=all_recipes, paginated_recipes=paginated_recipes,
                           random_recipes=random_recipes, limit=limit, current_pg=pg, sort=sort, lastpg=count,
                           all_count=all_count)


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
@app.route('/featured/', defaults={'pg': 1, 'limit': 8, 'sort': 1})
@app.route('/featured/<pg>/<limit>/<sort>')
def featured(pg, limit, sort):
    # all recipes
    all_recipes = DB_RECIPES.find()
    # all featured recipes
    featured_recipe_list = list(DB_RECIPES.find({'featured': 'true'}))
    # sorting
    sort = 1 if int(sort) == 1 else -1
    # pagination
    limit = int(limit)
    skip = 0 if int(pg) == 1 else (int(pg) - 1) * limit
    paginated_recipes = DB_RECIPES.find({'featured': 'true'}).sort([('name', sort)]).skip(skip).limit(limit)

    count = 0
    # calculate the last page number if not evenely divisible by the limmit
    for r_page in range(DB_RECIPES.count_documents({'featured': 'true'})):
        if r_page % limit == 0:
            count += 1

    featured_count = DB_RECIPES.count_documents({'featured': 'true'})
    return render_template('featured.html', all_recipes=all_recipes, paginated_recipes=paginated_recipes,
                           limit=limit, current_pg=pg, sort=sort, lastpg=count, featured_count=featured_count)


#########################
# FEATURED LIMIT AMOUNT #
#########################
@app.route('/featured_limit/', methods=['POST'])
def featured_limit():
    """Changes the number of recipes per page
        :param
        number selected
        :return
        featured with number per page
    """
    amount = int(request.form.get('amount'))
    return redirect(url_for('featured', pg=1, limit=amount, sort=1))


#################
# FEATURED SORT #
#################
@app.route('/featured_sort/<pg>/<limit>/', methods=['POST'])
def featured_sort(pg, limit):
    """Sorts recipes on the featured page
        :param
        number selected
        :return
        index with number per page
    """
    sort = int(request.form.get('sort'))

    return redirect(url_for('featured', pg=pg, limit=limit, sort=sort))


#############
# ALL VIEW #
############
@app.route('/all_recipes/', defaults={'pg': 1, 'limit': 8, 'sort': 1})
@app.route('/all_recipes/<pg>/<limit>/<sort>')
def all_recipes(pg, limit, sort):
    # all recipes
    all_recipes = DB_RECIPES.find()
    # all recipes count
    all_count = DB_RECIPES.count_documents({})
    # sorting
    sort = 1 if int(sort) == 1 else -1
    # pagination
    limit = int(limit)
    skip = 0 if int(pg) == 1 else (int(pg) - 1) * limit
    paginated_recipes = DB_RECIPES.find().sort([('name', sort)]).skip(skip).limit(limit)

    return render_template('all-recipes.html', all_recipes=all_recipes, paginated_recipes=paginated_recipes,
                           limit=limit, current_pg=pg, sort=sort, all_count=all_count)


####################
# ALL LIMIT AMOUNT #
####################
@app.route('/all_recipes_limit/', methods=['POST'])
def all_recipes_limit():
    """Changes the number of recipes per page
        :param
        number selected
        :return
        all recipes with number per page
    """
    amount = int(request.form.get('amount'))
    return redirect(url_for('all_recipes', pg=1, limit=amount, sort=1))


############
# ALL SORT #
############
@app.route('/all_recipes_sort/<pg>/<limit>/', methods=['POST'])
def all_recipes_sort(pg, limit):
    """Sorts recipes on the featured page
        :param
        number selected
        :return
        index with number per page
    """
    sort = int(request.form.get('sort'))

    return redirect(url_for('all_recipes', pg=pg, limit=limit, sort=sort))
