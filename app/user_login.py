import bcrypt
from flask import render_template, session, request, redirect, url_for

from app import app
from app.setup import MONGO, DB_USERS


#################
# REGISTER VIEW #
#################
@app.route('/register', methods=['POST', 'GET'])
def register():
    """ Renders the registration template and adds users credentials to the database
       :param
           user name (str) and password (str - hashed) received from the form element

       :return
           register.html if it is a GET request or if the username already exists
           profile.html if the username and password is sufficient

       """

    # REFERENCE CREDITS:
    # Login System ->
    # https://www.youtube.com/watch?v=vVx1737auSE, https://www.youtube.com/watch?v=PYILMiGxpAU
    #
    # Password Hashing ->
    # https://stackoverflow.com/questions/27413248/why-can-bcrypt-hashpw-be-used-both-for-hashing-and-verifying-passwords

    if request.method == 'POST':

        if request.form.get('confirm-password') != request.form.get('password'):
            return render_template('register.html', exists=False, mismatch_pw=True)

        # does user exist
        existing_user = DB_USERS.find_one({'username': request.form['username']})

        # user does not already exist
        if existing_user is None:
            # Hash the password for better security
            hashpass = bcrypt.hashpw(request.form.get('password').encode('utf-8'), bcrypt.gensalt())
            # Add the user to the database
            DB_USERS.insert({'username': request.form.get('username'), 'password': hashpass,
                             'profile_image': 'https://res.cloudinary.com/dajuujhvs/image/upload/v1592417238/xmt2q3ttok9cwjlux8j2.png',
                             'profile_image_id': 'xmt2q3ttok9cwjlux8j2',
                             'favorites': []})
            # create a session cookie
            session['USERNAME'] = request.form.get('username')
            # redirect to profile page
            return redirect(url_for('profile'))

        # User already exists
        else:
            return render_template('register.html', exists=True)

    # GET request
    return render_template('register.html', exists=False)


################
# SIGN-IN VIEW #
################
@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    """ Checks the username and password against the database and returns the appropriate html template
    :param
        user name (str) and password (str - hashed) received from the form element

    :return
        sign-in.html if it is a GET request or if the user has wrong username or password or
        profile.html if the username and password is correct

    """

    # REFERENCE CREDITS:
    # Login System ->
    # https://www.youtube.com/watch?v=vVx1737auSE, https://www.youtube.com/watch?v=PYILMiGxpAU
    #
    # Password Hashing ->
    # https://stackoverflow.com/questions/27413248/why-can-bcrypt-hashpw-be-used-both-for-hashing-and-verifying-passwords

    if request.method == 'POST':

        # search the database for the username
        login_user = MONGO.db.users.find_one({'username': request.form.get('username')})

        if login_user:
            # compare the hashed password in the database with the users entered password
            if bcrypt.hashpw(request.form.get('password').encode('utf-8'),
                             login_user['password']) == login_user['password']:
                session['USERNAME'] = request.form.get('username')
                # Login authentication success
                return redirect(url_for('profile'))

        # Login authentication failed
        return render_template('sign-in.html', failed=True)

    # GET request
    return render_template('sign-in.html', failf=False)


#################
# SIGN-OUT VIEW #
#################
@app.route('/sign-out')
def sign_out():
    """ Signs out the user by clearing the session cookie

        :return
            sign-in.html
        """

    # REFERENCE CREDITS:
    # Login System ->
    # https://www.youtube.com/watch?v=vVx1737auSE, https://www.youtube.com/watch?v=PYILMiGxpAU

    session.clear()
    return redirect(url_for('sign_in'))
