from app import app
from app.setup import DB_USERS, DB_RECIPES, DB_METHODS, DB_INGREDIENTS
from flask import render_template, session, redirect, url_for, abort, request
from bson.objectid import ObjectId
from cloudinary.uploader import upload, destroy


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

        return render_template('profile.html', user_data=existing_user, users_recipes=users_recipes)
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

