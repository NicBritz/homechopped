import os
from flask import Flask, render_template, session, request, redirect, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import cloudinary as cloudinary
from cloudinary.uploader import upload
from cloudinary.uploader import destroy
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
    return render_template('index.html', recipes=all_recipes)


# login routes
#
# Sign in page
@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    # This function renders the sign in template and checks the users credentials against the database.
    #
    # SRC - https://www.youtube.com/watch?v=vVx1737auSE && https://www.youtube.com/watch?v=PYILMiGxpAU

    # Creates a blank feedback message

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

        # if the request is a get then render the sign in template
        return render_template('sign-in.html', failed=True)

    # if the request is a get then render the sign in template
    return render_template('sign-in.html', failf=False)


# Registration Page
@app.route('/register', methods=['POST', 'GET'])
def register():
    # This function renders the registration template and adds users credentials to the database.
    #
    # SRC - https://www.youtube.com/watch?v=vVx1737auSE && https://www.youtube.com/watch?v=PYILMiGxpAU

    # Creates a blank feedback message

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
            db_users.insert({'username': request.form['username'], 'password': hashpass,
                             'profile_image': 'https://res.cloudinary.com/dajuujhvs/image/upload/v1591443059/xbv453shlvxycy399dcc.png',
                             'profile_image_id': 'xbv453shlvxycy399dcc'})
            session['USERNAME'] = request.form['username']
            return redirect(url_for('profile'))

        # if the user already exists
        else:
            return render_template('register.html', exists=True)

    # if it is a get request return registration template
    return render_template('register.html', exists=False)


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
        users_recipes = db_recipes.find({'author_id': existing_user['_id']})

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


# Update User profile
@app.route('/update-profile/<user_id>', methods=['POST'])
def update_profile(user_id):
    # This function uses the cloudinary framework yo upload a profile image and add it to the users profile
    #
    # src: https://github.com/tiagocordeiro/flask-cloudinary

    # users database variable
    db_users = mongo.db.users
    # get the file from the POST request
    file_to_upload = request.files['file']
    # upload the file and get the url of the uploaded file
    if file_to_upload:
        # find current user record
        current_user = db_users.find_one({'_id': ObjectId(user_id)})
        # find current image id
        current_image_id = current_user['profile_image_id']

        # delete the current image
        destroy(current_user['profile_image_id'], invalidate=True)
        # upload new image
        upload_result = upload(file_to_upload)

        #  update the profile picture of the users account and add it is user has no picture.
        db_users.update_one({'_id': ObjectId(user_id)},
                            {"$set": {'profile_image': upload_result['secure_url'],
                                      'profile_image_id': upload_result['public_id']}},
                            upsert=True)
    #  update the profile information and redirect to profile.
    db_users.update_one({'_id': ObjectId(user_id)},
                        {"$set": {'bio': request.form['bio'], 'email': request.form['email']}}, upsert=True)

    return redirect(url_for('profile'))


# Delete user profile
@app.route('/delete-user/<user_id>')
def delete_user(user_id):
    # deleted the user profile from the database
    #
    # users database variable
    db_users = mongo.db.users
    db_recipes = mongo.db.recipes
    db_ingredients = mongo.db.ingredients
    db_methods = mongo.db.methods
    db_recipes.delete_many({'author_id': ObjectId(user_id)})
    db_ingredients.delete_many({'author_id': ObjectId(user_id)})
    db_methods.delete_many({'author_id': ObjectId(user_id)})
    # delete the current image form cloudinary
    current_user = db_users.find_one({'_id': ObjectId(user_id)})
    destroy(current_user['profile_image_id'], invalidate=True)
    # delete the user
    db_users.remove({'_id': ObjectId(user_id)})
    return redirect(url_for('sign_out'))


# create temp recipe
@app.route('/add_temp_recipe/<user_id>')
def add_temp_recipe(user_id):
    db_recipes = mongo.db.recipes
    image_url = 'https://res.cloudinary.com/dajuujhvs/image/upload/v1591442613/pa9cybxloavqafbrktlf.png'
    image_url_id = 'pa9cybxloavqafbrktlf'
    db_recipes.insert_one(
        {
            'name': 'My Awesome Recipe',
            'image_url': image_url,
            'image_url_id': image_url_id,
            'featured': 'false',
            'current_rating': '0',
            'total_ratings': 0,
            'author_id': ObjectId(user_id)
        })
    current_recipe = db_recipes.find_one({'name': 'My Awesome Recipe'})
    return redirect(url_for('edit_recipe', user_id=user_id, recipe_id=current_recipe['_id']))


# edit recipe
@app.route('/edit_recipe/<user_id>/<recipe_id>')
def edit_recipe(user_id, recipe_id):
    db_recipes = mongo.db.recipes
    current_recipe = db_recipes.find_one({'_id': ObjectId(recipe_id)})
    db_ingredients = mongo.db.ingredients
    current_ingredients = db_ingredients.find({'recipe_id': current_recipe['_id']})
    db_methods = mongo.db.methods
    current_methods = db_methods.find({'recipe_id': current_recipe['_id']})
    return render_template('edit-recipe.html', user_id=user_id, recipe_id=recipe_id, current_recipe=current_recipe,
                           current_ingredients=current_ingredients, current_methods=current_methods)


# update recipe
@app.route('/update_recipe/<user_id>/<recipe_id>', methods=['POST'])
def update_recipe(user_id, recipe_id):
    current_user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    db_recipes = mongo.db.recipes

    # get the date
    today = date.today().strftime("%d/%m/%Y")

    # update record
    db_recipes.update_one({'_id': ObjectId(recipe_id)}, {"$set": {
        'name': request.form['recipe-name'],
        'description': request.form['recipe-description'],
        'notes': request.form['recipe-notes'],
        'preptime_hrs': request.form['prep-hours'],
        'preptime_min': request.form['prep-minutes'],
        'cooktime_hrs': request.form['cook-hours'],
        'cooktime_min': request.form['cook-minutes'],
        'serves': request.form['serves'],
        'author': current_user['username'],
        'author_id': ObjectId(user_id),
        'date_updated': today
    }}, upsert=True)
    return redirect(url_for('edit_recipe', _anchor='overview', user_id=user_id, recipe_id=recipe_id))


# Update recipe image
@app.route('/update_recipe_image/<user_id>/<recipe_id>', methods=['POST'])
def update_recipe_image(user_id, recipe_id):
    db_recipes = mongo.db.recipes
    current_recipe = db_recipes.find_one({'_id': ObjectId(recipe_id)})
    # get the date
    today = date.today().strftime("%d/%m/%Y")

    file_to_upload = request.files['file']
    # If no image is uploaded
    if file_to_upload.filename == '':
        # default url
        image_url = current_recipe['image_url']
        image_url_id = current_recipe['image_url_id']
    else:
        destroy(current_recipe['image_url_id'], invalidate=True)
        upload_result = upload(file_to_upload)
        image_url = upload_result['secure_url']
        image_url_id = upload_result['public_id']
        # update record
    db_recipes.update_one({'_id': ObjectId(recipe_id)}, {"$set": {
        'image_url': image_url,
        'image_url_id': image_url_id,
        'date_updated': today
    }}, upsert=True)
    return redirect(url_for('edit_recipe', _anchor='image', user_id=user_id, recipe_id=recipe_id))


# add ingredient item
@app.route('/add_ingredient_item/<user_id>/<recipe_id>', methods=['POST'])
def add_ingredient_item(user_id, recipe_id):
    db_recipes = mongo.db.recipes
    current_recipe = db_recipes.find_one({'_id': ObjectId(recipe_id)})
    # find any ingredients for this recipe
    db_ingredients = mongo.db.ingredients
    db_ingredients.insert_one(
        {'ingredient_item': request.form['ingredient_item'], 'recipe_id': current_recipe['_id'],
         'author_id': ObjectId(user_id)})
    return redirect(url_for('edit_recipe', _anchor='ingredients', user_id=user_id, recipe_id=recipe_id))


# delete ingredient item
@app.route('/delete_ingredient_item/<user_id>/<recipe_id>/<ingredient_id>')
def del_ingredient_item(user_id, recipe_id, ingredient_id):
    db_ingredients = mongo.db.ingredients
    db_ingredients.remove({'_id': ObjectId(ingredient_id)})
    return redirect(url_for('edit_recipe', _anchor='ingredients', user_id=user_id, recipe_id=recipe_id))


# delete recipe
@app.route('/delete_recipe/<recipe_id>')
def del_recipe(recipe_id):
    db_recipes = mongo.db.recipes
    db_recipes.remove({'_id': ObjectId(recipe_id)})
    db_ingredients = mongo.db.ingredients
    db_ingredients.delete_many({'recipe_id': ObjectId(recipe_id)})
    db_methods = mongo.db.methods
    db_methods.delete_many({'recipe_id': ObjectId(recipe_id)})
    return redirect(url_for('profile'))


# edit methods
@app.route('/edit_method_list/<user_id>/<recipe_id>', methods=['POST', 'GET'])
def edit_method_list(user_id, recipe_id):
    db_recipes = mongo.db.recipes
    current_recipe = db_recipes.find_one({'_id': ObjectId(recipe_id)})
    db_methods = mongo.db.methods
    current_methods = db_methods.find({'recipe_id': current_recipe['_id']})
    if request.method == 'POST':
        # find any methods for this recipe
        db_methods = mongo.db.methods
        db_methods.insert_one(
            {'method_name': request.form['method_name'], 'recipe_id': current_recipe['_id'],
             'author_id': ObjectId(user_id)})

    return render_template('edit-method-list.html', user_id=user_id, recipe_id=current_recipe['_id'],
                           current_methods=current_methods)


# add method item
@app.route('/add_method_item/<user_id>/<recipe_id>', methods=['POST'])
def add_method_item(user_id, recipe_id):
    db_recipes = mongo.db.recipes
    current_recipe = db_recipes.find_one({'_id': ObjectId(recipe_id)})
    db_methods = mongo.db.methods
    current_methods = db_methods.find({'recipe_id': current_recipe['_id']})

    # find any methods for this recipe
    db_methods = mongo.db.methods
    db_methods.insert_one(
        {'method_name': request.form['method_name'], 'recipe_id': current_recipe['_id'],
         'author_id': ObjectId(user_id)})
    return redirect(url_for('edit_recipe', _anchor='method', user_id=user_id, recipe_id=recipe_id))


# delete method item
@app.route('/delete_method_item/<user_id>/<recipe_id>/<method_id>')
def del_method_item(user_id, recipe_id, method_id):
    db_methods = mongo.db.methods
    db_methods.remove({'_id': ObjectId(method_id)})
    return redirect(url_for('edit_method_list', user_id=user_id, recipe_id=recipe_id))


# Recipe View
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    db_recipes = mongo.db.recipes
    current_recipe = db_recipes.find_one({'_id': ObjectId(recipe_id)})
    db_users = mongo.db.users
    current_recipe_author = db_users.find_one({'_id': ObjectId(current_recipe['author_id'])})
    db_ingredients = mongo.db.ingredients
    current_recipe_ingredients = db_ingredients.find({'recipe_id': ObjectId(recipe_id)})
    db_methods = mongo.db.methods
    current_recipe_methods = db_methods.find({'recipe_id': ObjectId(recipe_id)})
    return render_template('recipe.html', current_recipe=current_recipe, current_recipe_author=current_recipe_author,
                           current_recipe_ingredients=current_recipe_ingredients,
                           current_recipe_methods=current_recipe_methods)


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
