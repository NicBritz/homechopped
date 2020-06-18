import random

import pymongo
from flask import render_template, redirect, url_for, request, abort

from app import app
from app.setup import DB_RECIPES


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
    # variables
    count = 0

    # all recipes count
    all_count = DB_RECIPES.count_documents({})
    # all featured recipes
    featured_recipe_list = list(DB_RECIPES.find({'featured': 'true'}))
    # randomly select 4 from the featured
    random_recipes = random.sample(featured_recipe_list, k=4)

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

    # pagination calculation
    skip = 0 if int(pg) == 1 else (int(pg) - 1) * limit
    paginated_recipes = DB_RECIPES.find().sort([('name', sort)]).skip(skip).limit(limit)

    return render_template('index.html', all_recipes=DB_RECIPES.find(), paginated_recipes=paginated_recipes,
                           random_recipes=random_recipes, limit=limit, current_pg=pg, sort=sort, lastpg=count,
                           all_count=all_count)


######################
# INDEX LIMIT AMOUNT #
######################
@app.route('/index_limit/', methods=['POST'])
def index_limit():
    """ Changes the number of recipes per page
        :return
        index with number of recipes per page
    """
    try:
        # attempts to convert amount to an intiger
        amount = int(request.form.get('amount'))
    except:
        # raises a 404 error if any of these fail
        abort(404, description="Resource not found")

    return redirect(url_for('index', pg=1, limit=amount, sort=1, _anchor='recipe-list'))


##############
# INDEX SORT #
##############
@app.route('/index_sort/<pg>/<limit>/', methods=['POST'])
def index_sort(pg, limit):
    """Sorts recipes on the index page

    """
    try:
        # attempts to convert sort to an intiger
        sort = int(request.form.get('sort'))
    except:
        # raises a 404 error if any of these fail
        abort(404, description="Resource not found")

    return redirect(url_for('index', pg=pg, limit=limit, sort=sort, _anchor='recipe-list'))


#################
# FEATURED VIEW #
#################
@app.route('/featured/', defaults={'pg': 1, 'limit': 4, 'sort': 1})
@app.route('/featured/<pg>/<limit>/<sort>')
def featured(pg, limit, sort):
    """ Renders the featured view
        :return
        a view of featured recipes
        """
    # variables
    count = 0
    # all featured recipes count
    featured_count = DB_RECIPES.count_documents({'featured': 'true'})
    # all featured recipes
    featured_recipe_list = list(DB_RECIPES.find({'featured': 'true'}))

    # Error handeling
    try:
        # limits user to a valid limit range
        limit = int(limit)
        if limit > featured_count or limit < 2:
            # raises a 404 error if fail
            abort(404, description="Resource not found")

        # calculate the last page
        for r_page in range(featured_count):
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

    # pagination
    skip = 0 if int(pg) == 1 else (int(pg) - 1) * limit
    paginated_recipes = DB_RECIPES.find({'featured': 'true'}).sort([('name', sort)]).skip(skip).limit(limit)

    return render_template('featured.html', all_recipes=DB_RECIPES.find(), paginated_recipes=paginated_recipes,
                           limit=limit, current_pg=pg, sort=sort, lastpg=count, featured_count=featured_count)


#########################
# FEATURED LIMIT AMOUNT #
#########################
@app.route('/featured_limit/', methods=['POST'])
def featured_limit():
    """Changes the number of recipes per page

        :return
        featured with number per page
    """
    try:
        # attempts to convert amount to an intiger
        amount = int(request.form.get('amount'))
    except:
        # raises a 404 error if any of these fail
        abort(404, description="Resource not found")

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
    try:
        # attempts to convert sort to an intiger
        sort = int(request.form.get('sort'))
    except:
        # raises a 404 error if any of these fail
        abort(404, description="Resource not found")

    return redirect(url_for('featured', pg=pg, limit=limit, sort=sort))


#############
# ALL VIEW #
############
@app.route('/all_recipes/', defaults={'pg': 1, 'limit': 8, 'sort': 1})
@app.route('/all_recipes/<pg>/<limit>/<sort>')
def all_recipes(pg, limit, sort):
    """ Renders the all recipe view
            :return
            a view of all availible recipes
            """
    # variables
    count = 0
    # all recipes count
    all_count = DB_RECIPES.count_documents({})

    # Error handeling
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


    # pagination
    skip = 0 if int(pg) == 1 else (int(pg) - 1) * limit
    paginated_recipes = DB_RECIPES.find().sort([('name', sort)]).skip(skip).limit(limit)

    return render_template('all-recipes.html', all_recipes=DB_RECIPES.find(), paginated_recipes=paginated_recipes,
                           limit=limit, current_pg=pg, sort=sort, all_count=all_count, lastpg=count)


####################
# ALL LIMIT AMOUNT #
####################
@app.route('/all_recipes_limit/', methods=['POST'])
def all_recipes_limit():
    """Changes the number of recipes per page

        :return
        all recipes with number per page
    """
    try:
        # attempts to convert amount to an intiger
        amount = int(request.form.get('amount'))
    except:
        # raises a 404 error if any of these fail
        abort(404, description="Resource not found")

    return redirect(url_for('all_recipes', pg=1, limit=amount, sort=1))


############
# ALL SORT #
############
@app.route('/all_recipes_sort/<pg>/<limit>/', methods=['POST'])
def all_recipes_sort(pg, limit):
    """Sorts recipes on the featured page
        :return
        redirects to allrecipe
    """

    try:
        # attempts to convert sort to an intiger
        sort = int(request.form.get('sort'))
    except:
        # raises a 404 error if any of these fail
        abort(404, description="Resource not found")

    return redirect(url_for('all_recipes', pg=pg, limit=limit, sort=sort))


###############
# SEARCH VIEW #
##############
@app.route('/search_recipes/', methods=['POST', 'GET'])
def search_recipes():
    """Renders the search view and filter searched recipes.
        :return
        search view
    """

    if request.method == 'POST':
        result = DB_RECIPES.create_index([('name', pymongo.TEXT)])
        showing = request.form.get('search')
        search = DB_RECIPES.find({"$text": {"$search": request.form.get('search')}})
        search_count = DB_RECIPES.count_documents({"$text": {"$search": request.form.get('search')}})


        return render_template('search-recipes.html', all_recipes=DB_RECIPES.find(),
                               paginated_recipes=search, filtered=True, showing=showing, search_count=search_count)

    # all recipes count
    paginated_recipes = DB_RECIPES.find()
    return render_template('search-recipes.html', all_recipes=DB_RECIPES.find(), paginated_recipes=paginated_recipes)

