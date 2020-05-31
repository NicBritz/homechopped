import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# mongoDB config 
app.config["MONGO_DBNAME"] = os.environ.get('HC_MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('HC_MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html', recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
