from app import app
from flask import render_template, session, redirect, url_for, abort
from bson.objectid import ObjectId
from app.setup import DB_USERS, DB_RECIPES


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

