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


# temp

# users = {
#
#     'nic': {
#         'username': 'nic',
#         'password': '12345'
#     },
#     'sam': {
#         'username': 'sam',
#         'password': '54321'
#     }
# }


@app.route('/')
def index():
    # Returns the index.html and passes in all recipes from the database
    all_recipes = mongo.db.recipes.find()

    # SRC - https://www.youtube.com/watch?v=vVx1737auSE && https://www.youtube.com/watch?v=PYILMiGxpAU

    return render_template('index.html', recipes=all_recipes, )


@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        # search the database for the username
        login_user = mongo.db.users.find_one({'username': request.form.get('username')})

    if login_user:
        # compare hashed password src:
        # https://stackoverflow.com/questions/27413248/why-can-bcrypt-hashpw-be-used-both-for-hashing-and-verifying-passwords
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                         login_user['password']) == login_user['password']:
            session['USERNAME'] = request.form['username']
            return redirect(url_for('profile'))
    # failed
    return 'Invalid username/password combination'

    # if not username in users:
    #     print('username not found')
    #     return redirect(request.url)
    # else:
    #     # assign username from the form to the user var
    #     user = users[username]
    #
    # if not password == user['password']:
    #     print('password incorrect')
    #     return redirect(request.url)
    #
    # else:
    #     # store database id here!
    #     session['USERNAME'] = user['username']
    #     print('user added to session')
    #     return redirect(url_for('profile'))


# if request is a get request
return render_template('sign-in.html')


@app.route('/profile')
def profile():
    db_users = mongo.db.users
    # passed what it will become if not exist == None
    # if user exists
    if session.get('USERNAME', None) is not None:
        username = session.get("USERNAME")
        # get the user from the database
        existing_user = db_users.find_one({'username': username})
        print(existing_user)
        # userdata = users[username]
        return render_template('profile.html', userdata=existing_user)
    else:
        print('username not found in session')
        return redirect(url_for('sign_in'))


@app.route('/sign-out')
def sign_out():
    session.clear()
    return redirect(url_for('sign_in'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        db_users = mongo.db.users
        # check if user already exists
        existing_user = db_users.find_one({'username': request.form['username']})
        # if the user does not already exist
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # add to mongodb
            db_users.insert({'username': request.form['username'], 'password': hashpass})
            session['USERNAME'] = request.form['username']
            return redirect(url_for('profile'))
        else:
            return 'that username already exists!'
    # if it is a get request return registration template
    return render_template('register.html')


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
