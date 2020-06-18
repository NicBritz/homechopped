from bson.objectid import ObjectId
from cloudinary.uploader import upload, destroy
from flask import render_template, session, redirect, url_for, abort, request

from app import app
from app.setup import DB_USERS, DB_RECIPES, DB_METHODS, DB_INGREDIENTS


################
# PROFILE VIEW #
################
@app.route('/profile')
def profile():
    """ Directs user profile.html template if they are signed in, else to sign in page

    :return
        profile.html if the user is signed in
        sign-in.html if the user is not signed

    """

    # REFERENCE CREDITS:
    # Login System ->
    # https://www.youtube.com/watch?v=vVx1737auSE, https://www.youtube.com/watch?v=PYILMiGxpAU

    # User is signed in and exists in the database
    if session.get('USERNAME', None) is not None:
        username = session['USERNAME']

        # Fetch user and related recipes
        existing_user = DB_USERS.find_one({'username': username})
        users_recipes = DB_RECIPES.find({'author_id': existing_user['_id']})
        favorites = DB_RECIPES.find({'_id': {'$in': existing_user['favorites']}})

        return render_template('profile.html', user_data=existing_user, users_recipes=users_recipes,
                               favorites=favorites)
    else:
        # User not signed in
        return redirect(url_for('sign_in'))


#####################
# EDIT PROFILE VIEW #
#####################
@app.route('/edit-profile/<user_id>')
def edit_profile(user_id):
    """ Directs user profile.html template if they are signed in, else to sign in page

   :return
       users profile.html if the user is signed in
       sign-in.html if the user is not signed

    """
    # User exists in the database and Signed in
    if session.get('USERNAME', None) is not None:
        username = session['USERNAME']
        # user exists in the database
        current_user = DB_USERS.find_one({'username': username})
        requested_user = DB_USERS.find_one({'_id': ObjectId(user_id)})

        # if the current logged in user is the user requested
        if requested_user['_id'] == current_user['_id']:
            return render_template('edit-profile.html', user_data=requested_user)
        else:
            # Forbidden - User is not the account holder
            abort(403)
    else:
        # User not signed in
        return redirect(url_for('sign_in'))


##################
# UPDATE PROFILE #
##################
@app.route('/update-profile/<user_id>', methods=['POST'])
def update_profile(user_id):
    """ Updates the users db record with the POST form data, also updates the cloadinary image data

   :return
       Redirect to profile.html

    """
    # REFERENCE CREDITS:
    # Cloudinary api ->
    # https://github.com/tiagocordeiro/flask-cloudinary

    file_to_upload = request.files.get('file')

    if file_to_upload:
        # Current user record
        current_user = DB_USERS.find_one({'_id': ObjectId(user_id)})

        if current_user['profile_image_id'] != 'xmt2q3ttok9cwjlux8j2':
            # Remove current profile image
            destroy(current_user['profile_image_id'], invalidate=True)

        # Upload new image to cloudinary
        upload_result = upload(file_to_upload)

        # Update users profile image in DB
        DB_USERS.update_one({'_id': ObjectId(user_id)},
                            {"$set": {'profile_image': upload_result['secure_url'],
                                      'profile_image_id': upload_result['public_id']}},
                            upsert=True)

    #  Update users profile data
    DB_USERS.update_one({'_id': ObjectId(user_id)},
                        {"$set": {'bio': request.form.get('bio'), 'email': request.form.get('email')}}, upsert=True)

    return redirect(url_for('profile'))


##################
# DELETE PROFILE #
##################
@app.route('/delete-user/<user_id>')
def delete_user(user_id):
    """ Deletes the users db record , also Delete the cloadinary image data and all users recipe data

       :return
           Redirect to sign out url

        """
    # REFERENCE CREDITS:
    # Cloudinary api ->
    # https://github.com/tiagocordeiro/flask-cloudinary

    # Delete related user records
    DB_RECIPES.delete_many({'author_id': ObjectId(user_id)})
    DB_INGREDIENTS.delete_many({'author_id': ObjectId(user_id)})
    DB_METHODS.delete_many({'author_id': ObjectId(user_id)})

    # Delete the current user image form cloudinary
    current_user = DB_USERS.find_one({'_id': ObjectId(user_id)})
    destroy(current_user['profile_image_id'], invalidate=True)

    # Delete main user record
    DB_USERS.remove({'_id': ObjectId(user_id)})

    return redirect(url_for('sign_out'))


#################
# ADD FAVORITE  #
#################
@app.route('/add_favorite/<recipe_id>')
def add_favorite(recipe_id):
    """ Adds the recipe to the users favorites list in the users profile

     :return
         Redirect to recipe url with updated favorites list

    """
    updated_favorites = []
    # User is signed in and exists in the database
    if session.get('USERNAME', None) is not None:
        username = session['USERNAME']
        user = DB_USERS.find_one({'username': username})
        recipe = DB_RECIPES.find_one({'_id': ObjectId(recipe_id)})
        #  Update users favorites
        current_favorites = user['favorites']
        # if the recipe is not already in the list
        if ObjectId(recipe_id) not in current_favorites:
            current_favorites.append(ObjectId(recipe_id))

        DB_USERS.update_one({'_id': user['_id']},
                            {"$set": {'favorites': current_favorites, }}, upsert=True)

        updated_user = DB_USERS.find_one({'username': username})
        updated_favorites = updated_user['favorites']

    return redirect(url_for('recipe', recipe_id=recipe_id, favorites=updated_favorites))


####################
# REMOVE FAVORITE  #
###################
@app.route('/remove_favorite/<user_id>/<recipe_id>')
def remove_favorite(user_id, recipe_id):
    """ Removes the recipe from the users favorites list in the users profile
     :return
         Redirect to profile view with updated favorites list
    """

    user = DB_USERS.find_one({'_id': ObjectId(user_id)})
    current_favorites = user['favorites']
    current_favorites.remove(ObjectId(recipe_id))

    DB_USERS.update_one({'_id': user['_id']},
                        {"$set": {'favorites': current_favorites, }}, upsert=True)

    return redirect(url_for('profile'))
