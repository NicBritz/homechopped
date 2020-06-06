import os
from flask import Flask, render_template, session, request, redirect, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import cloudinary as cloudinary
from cloudinary.uploader import upload
import bcrypt
from datetime import date

# cloudinary config
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

app = Flask(__name__)

# mongoDB config
app.config["MONGO_DBNAME"] = os.environ.get('HC_MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('HC_MONGO_URI')

# secret key
app.config["SECRET_KEY"] = os.environ.get('SESSION_SECRET')

mongo = PyMongo(app)


@app.route('/')
def index():
    # Returns the index.html and passes in all recipes from the database
    #
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
    db_recipes = mongo.db.recipes

    # if user exists in the database and in the session variable
    if session.get('USERNAME', None) is not None:
        # assigns session var to username variable
        username = session['USERNAME']

        # get the user and users recipes from the database
        existing_user = db_users.find_one({'username': username})
        users_recipes = db_recipes.find({'author': username})

        return render_template('profile.html', user_data=existing_user, users_recipes=users_recipes)
    else:
        # if the user is not signed the are redirected to the sign in page
        return redirect(url_for('sign_in'))


# Sign out
@app.route('/sign-out')
def sign_out():
    # clears the session variables and redirects to the sign in page
    #
    session.clear()
    return redirect(url_for('sign_in'))


# Edit profile
@app.route('/edit-profile/<user_id>')
def edit_profile(user_id):
    # renders the edit profile page
    #
    # create a variable of the users database
    db_users = mongo.db.users

    # get the user from the database
    user_data = db_users.find_one({'_id': ObjectId(user_id)})

    return render_template('edit-profile.html', user_data=user_data)


# upload profile image
@app.route('/upload-profile-image/<user_id>', methods=['POST'])
def upload_profile_image(user_id):
    # This function uses the cloudinary framework yo upload a profile image and add it to the users profile
    #
    # src: https://github.com/tiagocordeiro/flask-cloudinary

    # users database variable
    db_users = mongo.db.users
    # get the file from the POST request
    file_to_upload = request.files['file']
    # upload the file and get the url of the uploaded file
    if file_to_upload:
        upload_result = upload(file_to_upload)
        url = upload_result['secure_url']
        #  update the profile picture of the users account and add it is user has no picture.
        db_users.update_one({'_id': ObjectId(user_id)}, {"$set": {'profile_image': url}}, upsert=True)

    return redirect(url_for('edit_profile', user_id=user_id))


# Update User profile
@app.route('/update-profile/<user_id>', methods=['POST'])
def update_profile(user_id):
    # Updates the user profile information

    # users database variable
    db_users = mongo.db.users
    #  update the profile information and redirect to profile.
    db_users.update_one({'_id': ObjectId(user_id)}, {"$set": {'bio': request.form['bio']}}, upsert=True)

    return redirect(url_for('profile'))


# Delete user profile
@app.route('/delete-user/<user_id>')
def delete_user(user_id):
    # deleted the user profile from the database
    #
    # users database variable
    db_users = mongo.db.users
    #  update the profile information and redirect to profile.
    db_users.remove({'_id': ObjectId(user_id)})

    return redirect(url_for('sign_out'))


# Add recipe
@app.route('/add-recipe/<user_id>', methods=['POST', 'GET'])
def add_recipe(user_id):
    # users database variable
    current_user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    db_recipes = mongo.db.recipes

    if request.method == 'POST':
        # upload image and get the url
        image_url = None
        file_to_upload = request.files['file']
        # If no image is uploaded
        if file_to_upload.filename == '':
            # default url
            image_url = 'https://res.cloudinary.com/dajuujhvs/image/upload/v1591433093/homechopped/photo-placeholder-icon-6_q4zywi.png'
        else:
            upload_result = upload(file_to_upload)
            image_url = upload_result['secure_url']

        # prep time calc
        prep_time = f"{request.form['prep-hours']}h : {request.form['prep-minutes']}m"
        # cook time calc
        cook_time = f"{request.form['cook-hours']}h : {request.form['cook-minutes']}m"

        #get the date
        today = date.today().strftime("%d/%m/%Y")

        # insert record
        db_recipes.insert_one({
            'image_url': image_url,
            'name': request.form['recipe-name'],
            'description': request.form['recipe-description'],
            'notes': request.form['recipe-notes'],
            'preptime': prep_time,
            'cooktime': cook_time,
            'serves': request.form['serves'],
            'author': current_user['username'],
            'featured': 'false',
            'current_rating': '0',
            'total_ratings': 0,
            'date_created': today
        })
        return redirect(url_for('profile'))

    return render_template('add-recipe.html')


@app.route('/featured/<sortby>')
def featured_sorted(sortby):
    # Returns the featured.html and passes in featured recipes from the database
    #
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
