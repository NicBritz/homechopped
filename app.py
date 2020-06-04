import os
from flask import Flask, render_template, session, request, redirect, url_for
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

# mongoDB config 
app.config["MONGO_DBNAME"] = os.environ.get('HC_MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('HC_MONGO_URI')

# secret key
app.config["SECRET_KEY"] = "uF_a0HhS1HAneZoA0XeGw"

mongo = PyMongo(app)


@app.route('/')
def index():
    # Returns the index.html and passes in all recipes from the database
    all_recipes = mongo.db.recipes.find()
    return render_template('index.html', recipes=all_recipes, )


# login routes
#
# Sign in page
@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    # This function renders the sign in template and checks the users credentials against the database.
    #
    # SRC - https://www.youtube.com/watch?v=vVx1737auSE && https://www.youtube.com/watch?v=PYILMiGxpAU

    # Creates a blank feedback message
    message = ''
    if request.method == 'POST':

        # search the database for the username
        login_user = mongo.db.users.find_one({'username': request.form.get('username')})

        if login_user:
            # compare the hashed password in the database with the users entered password src:
            # https://stackoverflow.com/questions/27413248/why-can-bcrypt-hashpw-be-used-both-for-hashing-and-verifying-passwords
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                             login_user['password']) == login_user['password']:
                session['USERNAME'] = request.form['username']
                return redirect(url_for('profile'))
        # authentication failed
        message = 'Invalid username or password.'

    # if the request is a get then render the sign in template
    return render_template('sign-in.html', message=message)


# Registration Page
@app.route('/register', methods=['POST', 'GET'])
def register():
    # This function renders the registration template and adds users credentials to the database.
    #
    # SRC - https://www.youtube.com/watch?v=vVx1737auSE && https://www.youtube.com/watch?v=PYILMiGxpAU

    # Creates a blank feedback message
    message = ''
    if request.method == 'POST':
        # create a variable of the users database
        db_users = mongo.db.users

        # check if user already exists
        existing_user = db_users.find_one({'username': request.form['username']})

        # if the user does not already exist
        if existing_user is None:

            # if password is less than 5 characters
            if len(request.form['password']) < 5:
                message = 'Password must be at least 5 characters long.'
                return render_template('register.html', message=message)
            # Hash the password for better security
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # add record to mongodb
            db_users.insert({'username': request.form['username'], 'password': hashpass})
            session['USERNAME'] = request.form['username']
            return redirect(url_for('profile'))
        # if the user already exists
        else:
            message = 'username already exists.'
            return render_template('register.html', message=message)

    # if it is a get request return registration template
    return render_template('register.html', message=message)


# Profile page
@app.route('/profile')
def profile():
    # Directs the user to the main profile page
    #
    # create a variable of the users database
    db_users = mongo.db.users

    # if user exists in the database and in the session variable
    if session.get('USERNAME', None) is not None:
        # assigns session var to username variable
        username = session['USERNAME']

        # get the user from the database
        existing_user = db_users.find_one({'username': username})

        return render_template('profile.html', userdata=existing_user)
    else:
        # if the user is not signed the are redirected to the sign in page
        return redirect(url_for('sign_in'))

# Sign out
@app.route('/sign-out')
def sign_out():
    # clears the session variables and redirects to the sign in page
    session.clear()
    return redirect(url_for('sign_in'))


@app.route('/featured/<sortby>')
def featured_sorted(sortby):
    # Returns the featured.html and passes in featured recipes from the database
    # with a variable for some sorting options
    featured_recipes = None
    if sortby == 'a-z':
        featured_recipes = mongo.db.recipes.find({'featured': 'true'}).sort([('name', 1)])
        a_to_z = 'a-z'
    elif sortby == 'z-a':
        featured_recipes = mongo.db.recipes.find({'featured': 'true'}).sort([('name', -1)])
        a_to_z = 'z-a'
    return render_template('featured.html', recipes=featured_recipes, a_to_z=a_to_z)


if __name__ == '__main__':
    app.secret_key = 'my_secret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
