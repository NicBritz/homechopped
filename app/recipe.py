from app import app
from app.setup import DB_RECIPES, DB_INGREDIENTS, DB_METHODS, DB_USERS, TODAY_STR
from flask import redirect, url_for, render_template, request
from bson.objectid import ObjectId
from cloudinary.uploader import upload, destroy


####################
# MAIN RECIPE VIEW #
####################
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """ Returns the main recipe view

     :return
         Renders recipe.html

    """
    current_recipe = DB_RECIPES.find_one({'_id': ObjectId(recipe_id)})
    current_recipe_author = DB_USERS.find_one({'_id': ObjectId(current_recipe['author_id'])})
    current_recipe_ingredients = DB_INGREDIENTS.find({'recipe_id': ObjectId(recipe_id)})
    current_recipe_methods = DB_METHODS.find({'recipe_id': ObjectId(recipe_id)})

    return render_template('recipe.html', current_recipe=current_recipe, current_recipe_author=current_recipe_author,
                           current_recipe_ingredients=current_recipe_ingredients,
                           current_recipe_methods=current_recipe_methods)


###############
# TEMP RECIPE #
###############
@app.route('/add_temp_recipe/<user_id>')
def add_temp_recipe(user_id):
    """ Creates a temporary recipe record to assign to the user

     :return
         Redirect to edit_recipe url

    """

    # Default recipe image
    image_url = 'https://res.cloudinary.com/dajuujhvs/image/upload/v1591442613/pa9cybxloavqafbrktlf.png'
    image_url_id = 'pa9cybxloavqafbrktlf'

    temp_record = DB_RECIPES.insert_one(
        {
            'name': 'My Awesome Recipe',
            'image_url': image_url,
            'image_url_id': image_url_id,
            'featured': 'false',
            'current_rating': '0',
            'total_ratings': 0,
            'author_id': ObjectId(user_id)
        })

    return redirect(url_for('edit_recipe', user_id=user_id, recipe_id=temp_record.inserted_id))


####################
# EDIT RECIPE VIEW #
####################
@app.route('/edit_recipe/<user_id>/<recipe_id>')
def edit_recipe(user_id, recipe_id):
    """ Renders the edit-recipe template passing in the temporary recipe id

     :return
         returns the edit-recipe.html form

    """
    current_recipe = DB_RECIPES.find_one({'_id': ObjectId(recipe_id)})
    current_ingredients = DB_INGREDIENTS.find({'recipe_id': current_recipe['_id']})
    current_methods = DB_METHODS.find({'recipe_id': current_recipe['_id']})

    return render_template('edit-recipe.html', user_id=user_id, recipe_id=recipe_id, current_recipe=current_recipe,
                           current_ingredients=current_ingredients, current_methods=current_methods)


#################
# UPDATE RECIPE #
#################
@app.route('/update_recipe/<user_id>/<recipe_id>', methods=['POST'])
def update_recipe(user_id, recipe_id):
    """ Updates the recipe database record

    :return
        returns the edit-recipe.html form overview tab

    """
    # get the current user's record
    current_user = DB_USERS.find_one({'_id': ObjectId(user_id)})

    # update the recipe record
    DB_RECIPES.update_one({'_id': ObjectId(recipe_id)}, {"$set": {
        'name': request.form.get('recipe-name'),
        'description': request.form.get('recipe-description'),
        'notes': request.form.get('recipe-notes'),
        'preptime_hrs': request.form.get('prep-hours'),
        'preptime_min': request.form.get('prep-minutes'),
        'cooktime_hrs': request.form.get('cook-hours'),
        'cooktime_min': request.form.get('cook-minutes'),
        'serves': request.form.get('serves'),
        'author': current_user['username'],
        'author_id': ObjectId(user_id),
        'date_updated': TODAY_STR
    }}, upsert=True)
    # return to recipe overview page
    return redirect(url_for('edit_recipe', _anchor='overview', user_id=user_id, recipe_id=recipe_id))


#######################
# UPDATE RECIPE IMAGE #
#######################
@app.route('/update_recipe_image/<user_id>/<recipe_id>', methods=['POST'])
def update_recipe_image(user_id, recipe_id):
    """ Updates the recipe image in cloudinary

    :return
        returns the edit-recipe.html form image tab with updated image

    """

    # get the file from the form
    file_to_upload = request.files.get('file')

    if file_to_upload:
        # get the current recipe record
        current_recipe = DB_RECIPES.find_one({'_id': ObjectId(recipe_id)})
        # delete the current recipe image on cloudinary
        destroy(current_recipe['image_url_id'], invalidate=True)
        # upload the new image
        upload_result = upload(file_to_upload)

        # update record
        DB_RECIPES.update_one({'_id': ObjectId(recipe_id)}, {"$set": {
            'image_url': upload_result['secure_url'],
            'image_url_id': upload_result['public_id'],
            'date_updated': TODAY_STR
        }}, upsert=True)

    return redirect(url_for('edit_recipe', _anchor='image', user_id=user_id, recipe_id=recipe_id))


#################
# DELETE RECIPE #
#################
@app.route('/delete_recipe/<recipe_id>')
def del_recipe(recipe_id):
    """ Deletes the recipe from the database

   :return
       Redirects to the user's profile url

   """
    DB_RECIPES.remove({'_id': ObjectId(recipe_id)})
    DB_INGREDIENTS.delete_many({'recipe_id': ObjectId(recipe_id)})
    DB_METHODS.delete_many({'recipe_id': ObjectId(recipe_id)})

    return redirect(url_for('profile'))


##################
# ADD INGREDIENT #
##################
@app.route('/add_ingredient_item/<user_id>/<recipe_id>', methods=['POST'])
def add_ingredient_item(user_id, recipe_id):
    """ Adds an ingredient to the database and references the recipe id

    :return
        returns the edit-recipe.html form ingredient tab with updated ingredient list

    """
    # Insert ingredient record
    DB_INGREDIENTS.insert_one(
        {'ingredient_item': request.form.get('ingredient_item'), 'recipe_id': ObjectId(recipe_id),
         'author_id': ObjectId(user_id)})

    return redirect(url_for('edit_recipe', _anchor='ingredients', user_id=user_id, recipe_id=recipe_id))


#####################
# DELETE INGREDIENT #
#####################
@app.route('/delete_ingredient_item/<user_id>/<recipe_id>/<ingredient_id>')
def del_ingredient_item(user_id, recipe_id, ingredient_id):
    """ Deletes an ingredient to the database from the recipe id reference

    :return
        returns the edit-recipe.html form ingredient tab with updated ingredient list

    """
    # Remove ingredient record
    DB_INGREDIENTS.remove({'_id': ObjectId(ingredient_id)})

    return redirect(url_for('edit_recipe', _anchor='ingredients', user_id=user_id, recipe_id=recipe_id))


###################
# ADD METHOD ITEM #
###################
@app.route('/add_method_item/<user_id>/<recipe_id>', methods=['POST'])
def add_method_item(user_id, recipe_id):
    """ Adds a method to the database and references the recipe id

    :return
        returns the edit-recipe.html form method tab with updated method list

    """
    # Insert method record
    DB_METHODS.insert_one(
        {'method_name': request.form.get('method_name'), 'recipe_id': ObjectId(recipe_id),
         'author_id': ObjectId(user_id)})

    return redirect(url_for('edit_recipe', _anchor='method', user_id=user_id, recipe_id=recipe_id))


######################
# DELETE METHOD ITEM #
######################
@app.route('/delete_method_item/<user_id>/<recipe_id>/<method_id>')
def del_method_item(user_id, recipe_id, method_id):
    """ Deletes an method to the database from the recipe id reference

        :return
            returns the edit-recipe.html form method tab with updated method list

        """
    # Remove method record
    DB_METHODS.remove({'_id': ObjectId(method_id)})

    return redirect(url_for('edit_recipe', _anchor='method', user_id=user_id, recipe_id=recipe_id))
