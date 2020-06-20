

[![alt text](https://res.cloudinary.com/dajuujhvs/image/upload/v1592435629/homechopped/logo_satpdh.png)](http://homechopped.herokuapp.com/)

------

## Overview

Home chopped is a user driven recipe web site where you are able share your ideas for delicious dishes. You can also rate recipes offered by other users and even add recipes to your collection of favourites for easy recall at a later stage. 

If your recipe is chosen to be one of our featured recipes there is a chance that it will be presented on the main page slider section. 

Recipes are displayed in the form of cards with the main focus being the image and the recipe name. From there users are able to use the `more` icon to view some additional key information about your recipe. The user can either select the `VIEW` or select any of the pictures of your recipe to see the full recipe.

The recipe section is easy to navigate and from this view your recipe can be shared or printed, this is also where a user is able to rate or favourite your recipe. 

There is also a secure user profile area where you are able to add recipes as well as edit your existing recipes. From here you can also edit you user profile and even change your profile image.

------

## Table of Contents

[TOC]



----



## UX

### User

As a user I would like...

- to be able share my recipes with the world
- to view other users recipes with easy ways to navigate an filter them
- an application that is available on multiple platforms for ease of use
- the application to be easy to navigate with icons and other visual ques
- a rating system where others can rate my dish
- to share my recipes to popular platforms i.e. - Facebook, twitter, Pinterest
- a way to print my recipe to use when I am not able to get online
- a login area that securely stores a hashed version of my password and shows my username in the navigation bar when I am logged in
- a user profile area where I am able to manage my recipes, favourites and my user profile
- to change my user profile image as well as write a small bio about me
- a way to edit and delete recipes I have made
- to be able to delete my profile and all associated recipes with one button

### Design

The goal of this project was the create a user driven recipe website that uses a MongoDB database in the backend to manage the core data. The site is neat, clean and responsive and makes use of the full CRUD functionality in various areas. 

### Wireframes

Before starting the project I used [Balsamiq](https://balsamiq.com/) to create the following wireframes. The licence for the software was provided by the Code Institute. Here You can find my [Balsamiq project file](docs) as well as higher resolution images.

#### Home page

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592316322/homechopped/index_all_cdteer.png" alt="home wireframes" style="zoom:50%;" />

#### Filtered pages

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592316322/homechopped/pages_all_akmbkl.png" alt="filtered wireframes" style="zoom:50%;" />

#### Recipe page

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592316322/homechopped/recipe_all_xbl8mu.png" alt="recipe wireframes" style="zoom:50%;" />

#### Edit pages

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592316322/homechopped/edit_views_nvaemv.png" alt="edit wireframes" style="zoom:50%;" />

### Trello

To keep track of the project I made use of a Trello board. The board was used to keep track of progress add ideas when they spring to mind and keep track of online resourses. You can view the board [here](https://trello.com/b/8o2Zv6LB/ci-milestone-3-homechopped)

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592319213/homechopped/Trello_ggwwzf.png" alt="trello screenshot" style="zoom:33%;" />

### Database Schema

The database I used for this project was MongoDB hosted through [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) below is a screenshot of the schema.



![](https://res.cloudinary.com/dajuujhvs/image/upload/v1592402717/homechopped/DB_Visualization_oau0fj.png)



## Features

### The  navigation bar

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592401733/homechopped/nav-bar_ckcv0x.png" alt="navbar screenshot" style="zoom:33%;" />

I created a simple favicon ![favicon](https://res.cloudinary.com/dajuujhvs/image/upload/v1592435482/homechopped/favicon_p5jxuk.png)for the browser tab this was just to help make the site feel a bit more finished. In the navigation bar I have created a simple logo using CSS styling as this is a pretty simple logo. There are some links to at the top of the page to different sections of the site that will highlight depending on the screen you are in. I have also included an icon that will display the word 'login' if the user is not logged in and will display the username if the user is logged in. When browsing the site on a mobile device, the navbar will be replaced with a bars icon <img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592401861/homechopped/bars_m13wxv.png" style="zoom:30%;" />  that will reveal a side navigation pane with icons and links to each section.

### Main Slider

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592402000/homechopped/slider_akhtzs.png" alt="main slider screenshot" style="zoom:30%;" />

At the top of my home page I have a large slider this is to create an eye-catching first impression. The slider will randomly choose four recipes from the pool of featured recipes each time the page is refreshed. The image for each recipe is accompanied by a banner with the recipe name that animates in from the top. If you select the image of any of the recipes you will be directed to that recipes page.

### View  filtering

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592403147/homechopped/sorting_a3vv9d.png" alt="filtering screenshot" style="zoom:50%;" />

Above the list of recipe cards are filter options, this includes choosing the amount of cards to show at a time as well as some sorting options. These options are setup to submit on change for convenience.

### Recipe cards

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592403608/homechopped/recipe_card_gp9pci.png" alt="recipe cards screenshot" style="zoom:50%;" />

The recipe cards are designed to look simplistic with a large picture and the recipe title underneath. There is a 'more' icon that can be used to reveal some more key information about the recipe. You can get to the complete recipe either by clicking the `VIEW` link or the recipe image.

### Pagination

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592403436/homechopped/pagination_ed8dww.png" alt="pagination screenshot" style="zoom:50%;" />

Recipe cards are displayed with pagination navigation at the bottom of the page, this changes depending on the number of cards set to display. This also highlights the page you are currently on. The pagination section has chevrons that can be used for next and previous page and will disable at either end. 

### Footer

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592404542/homechopped/footer_zvtwaw.png" alt="footer screenshot" style="zoom:33%;" />

The footer is purposefully simple to not take away from the  main recipe area, here you will find the links to our social pages.

### Sign-in

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592404832/homechopped/Signin_pgrtr8.png" alt="sign in screenshot" style="zoom:50%;" />

The sign in page is simple, users can enter their username and password. This is authenticated in python and feedback is given if the credentials are incorrect. For security all passwords are hashed and the hashed versions are compared. Successfully signing in to the site will direct the user to their profile page. There is also a link here to register a new user.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592405293/homechopped/logged_in_smbdns.png" alt="logged in screenshot" style="zoom:50%;" />

Logged in users will have their username displayed in the navigation bar to show the login status.

 ### Registration

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592405541/homechopped/register_osbrar.png" alt="registration screenshot" style="zoom:50%;" />

Registration is a similar process to signing in. The form is set to give feedback if username is too short. There is also error checking against confirmation password mismatch and some basic password criteria. Passwords are hashed using  [bcrypt](https://github.com/pyca/bcrypt/) and then saved to the database, hashed passwords are compared on login attempt. Once registered the user ill be redirected to their profile page. There is also a link to go to the sign in page here.

### Profile page

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592406084/homechopped/Profile_Page_qiempa.png" alt="profile page screenshot" style="zoom:33%;" />

The profile page is a users space to edit and manage their site presence. There are icons with tooltips to help the user navigate easily. From this view the user is able to add and edit recipes and sign out of the site.

### Edit profile

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592406356/homechopped/edit_profile_sqwhzk.png" alt="edit profile screenshot" style="zoom:37%;" />

Editing your profile could not be easier, with intuitive icons and tooltips. In the edit profile view you can upload an image, write a small bio about yourself and add your email address. 

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592408050/homechopped/delete_profile_x4kp7m.png" alt="delete profile screenshot" style="zoom:50%;" />

This is also where you will delete your profile. Deleting your profile will also delete all your recipes and images so you will be asked to confirm before the delete is executed.

### Create / Edit recipe

#### Image tab

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592408366/homechopped/edit_recipe_image_dmche0.png" alt="image tab screenshot" style="zoom:33%;" />

Editing the recipe image is simple with a full size preview. When changing out an image the old image is automatically removed from the CDN using [cloudinary's](https://cloudinary.com/) python package. This is also set to submit on change for instant feedback.

#### Recipe info tab

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592408633/homechopped/edit_recipe_info_vwy9ol.png" alt="info tab screenshot" style="zoom:33%;" />

Here you can add the main information about your recipe. This includes timing information, serving information and a description of your recipe. this is also where the recipe's name is edited. Deleting a recipe is also managed from this tab with the same confirmation modal as deleting a user profile. 

#### Ingredient and Method tabs

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592408877/homechopped/edit_ingredients_uxox4i.png" alt="ingredient screenshot" style="zoom:33%;" />

Here you can add or delete recipe ingredients as needed. There is a large add icon and a text field to insert records and items can be deleted in any order.

### Recipe view

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592409139/homechopped/Recipe_main_afk0lk.png" alt="recipe screenshot" style="zoom:33%;" />

The main recipe view is what will be used to make the dish so this has all the features. Author information and the last date it was updated are displayed here along with the recipe's current rating.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592409412/homechopped/rate_pgqwrc.png" alt="rating screenshot" style="zoom:50%;" />

Recipe's can be rated here and there is calculation in the backend managing the rating system. Currently I have made this so that any visitor or registered user can rate a recipe but this can easily be switched to registered users only.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592409847/homechopped/fav_kmqllf.png" alt="favourite screenshot" style="zoom:80%;" />

A logged in user is able to favourite recipes, if you are viewing a recipe that you have favourited it will have a red icon.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592410006/homechopped/share_hdsuva.png" alt="share screenshot" style="zoom:80%;" />

The share button is setup to share the recipe to some popular social platforms, the links are working and will share the recipe if you are logged in.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592410260/homechopped/Print_dbtcoj.png" alt="print screenshot" style="zoom:33%;" />

If you are in need pf a printed version of the recipe there is a print button setup for that. I have used custom classes to manage the printed content.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592410411/homechopped/ingmet_jpxand.png" alt="ingredients screenshot" style="zoom:33%;" />

The ingredient and methods are styled accordingly, for example the methods have numbered steps where the ingredients do not. These step numbers are created using jinja templating.

### Code structure

After some time of adding features to the project I decided to split the Code into more manageable files. this helped a lot as the project grew in scale. below is an outline of this file / folder structure.

```bash
.
├── static
│   ├── css
│   │   ├── card.css
│   │   ├── errors.css
│   │   ├── index.css
│   │   ├── print-recipe.css
│   │   ├── recipe.css
│   │   └── style.css
│   ├── images
│   │   ├── favicon.ico
│   │   └── favicon.png
│   └── js
│       └── app.js
├── templates
│   ├── 403.html
│   ├── 404.html
│   ├── 410.html
│   ├── 500.html
│   ├── all-recipes.html
│   ├── base.html
│   ├── edit-method-list.html
│   ├── edit-profile.html
│   ├── edit-recipe.html
│   ├── featured.html
│   ├── index.html
│   ├── profile.html
│   ├── recipe.html
│   ├── register.html
│   └── sign-in.html
├── tests
│   ├── ./tests/__init__.py
│   ├── ./tests/test_login.py
│   ├── ./tests/test_profile.py
│   ├── ./tests/test_recipe.py
│   └── ./tests/test_views.py
├── __init__.py
├── errors.py
├── recipe.py
├── setup.py
├── user_login.py
├── user_profile.py
└── views.py

```

### Features Left to Implement

- multiple ingredient lists for a complex recipe
- more sorting and filtering options
- recipe categories
- About the author section

---

## Technologies Used

The following is a list of tools and technologies I used to create this website:

- [Flask 1.1.2](https://palletsprojects.com/p/flask/)
  - Used as the main framework for my application
- [Python 3.8.3](https://www.python.org/)
  - Used for backend data manipulation
- [Pymongo 3.10.1](https://docs.mongodb.com/drivers/pymongo)
  - Used to communicate with the mongoDB database
- [Pytest 5.4.3](https://pypi.org/project/pytest/)
  - Used for unit testing my application
- [Jinja2 2.11.2](https://pypi.org/project/Jinja2/)
  - Used as the main templating language for template manipulation
- [Cloudinary 1.21.0](https://cloudinary.com/)
  - Used to access the Cloudinary CDN server for image management
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
  - Used as the main language for the templates
- [CSS3](https://www.w3.org/Style/CSS/current-work.en.html)
  - Used for styling the webpage
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used for some front end functionality
- [Git](https://git-scm.com/)
  - Used for version control
- [Materialize](https://materializecss.com/)
  - Used as the main frontend framework
- [Google fonts](https://fonts.google.com/)
  - Used for website fonts
- [Font Awesome](https://fontawesome.com/)
  - Used for some icons on the website
- [Heroku](https://www.heroku.com/)
  - Used to host the website
- [GitHub](https://github.com/)
  - Used to store my project source code
- [MongoDB](https://www.mongodb.com/cloud/atlas)
  - Used as the main database technology

### Other Tools

- [Pycharm](https://www.jetbrains.com/pycharm/)
  - This is the main IDE I used to build the website.
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html?gclid=CjwKCAjwvOHzBRBoEiwA48i6AtbSWstaKzHCUaUKzSlnKYFxv7dELw1rAOJgZhYShhzdXSxrCp3JHxoCnG4QAvD_BwE&sdid=88X75SKR&mv=search&ef_id=CjwKCAjwvOHzBRBoEiwA48i6AtbSWstaKzHCUaUKzSlnKYFxv7dELw1rAOJgZhYShhzdXSxrCp3JHxoCnG4QAvD_BwE:G:s&s_kwcid=AL!3085!3!340669891884!e!!g!!photoshop)
  - Used to manipulate and create content for the website.
- [Balsamq](https://balsamiq.com/) 
  - Used to create wireframes for the website.
- [VS Code](https://code.visualstudio.com/) 
  - Used for some coding due to its wide range of add-ins.
- [Grammarly](https://www.grammarly.com/)
  - Used to double-check all my spelling and grammar.
- [W3C Markup](https://validator.w3.org/)
  - Used this to check my HTML for errors and typos.
- [W3C CSS](https://jigsaw.w3.org/css-validator/)
  - Used this to check the validity of my CSS.
- [jshint](https://jshint.com/)
  - Used to validate JavaScript.
- [Autoprefixer](https://autoprefixer.github.io/)
  - I used this tool to make sure I did not miss any prefixing in my code.

------



## Testing

Testing and error checking was undertaken throughout the development process. With the aid of the following tools and the help of human testers, I was able to catch and fix errors and bugs in my code.

#### [W3C Markup](https://validator.w3.org/)

Even though using this validator would understandably show errors for the jinja code i managed to catch some small mistakes by validating all the individual html files.

####  [W3C CSS](https://jigsaw.w3.org/css-validator/)

I tested all the CSS files in the project using W3C CSS validator with no errors as per image below.

![](https://res.cloudinary.com/dajuujhvs/image/upload/v1592421296/homechopped/valid_s0xh6m.png)

#### [Autoprefixer](https://autoprefixer.github.io/)

After finishing up my CSS and before the validation of CSS I used this tool to make sure I had not left out any prefixing in my code.

#### Unit Testing

I used [pytest](https://docs.pytest.org/en/stable/) for unit testing, you can fins a copy of my tests in the tests folder in the main app. I only wrote the basic response tests but they ended up helping me a lot when I was developing error handling. To manually run the tests you can run the command ``py.test``. You can find all my unit tests [here](app/tests).

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592601487/homechopped/Pytest_a8tv6f.png" style="zoom:50%;" alt="pytest results "/>

#### CI/CD

As an extra test I used [github actions](https://github.com/features/actions) to set up continuous integration tests when ever I create a pull request. This was just in case I broke something. It was good to check before merging to the master branch.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592601810/homechopped/CICD_yhio1h.png" style="zoom:60%;" alt="ci/cd picture"/>

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592601947/homechopped/cicd2_c5xjzm.png" style="zoom:50%;" alt="github actions screenshot" />

#### Google Lighthouse

I used google lighthouse in the chrome browser to help improve performance and catch errors, I fins this a very useful tool to catch small mistakes like forgetting an alt tag for images. 

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592602983/homechopped/chrome_lighthouse_e63o78.png" style="zoom:60%;" alt="google lighthouse results" />

#### Browser and Device Testing

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :--------- | :----------------------------------------------------------- | :--------------------- |
| Google Chrome    | PC         | Excellent                                                    | Version 83.0.4103.106  |
| Firefox          | PC         | Excellent                                                    | Version 77.0.1         |
| Microsoft Edge   | PC         | Excellent                                                    | Version 83.0.478.54    |
| IE 11            | PC         | Good - slight styling differences, some share links are not supported due to depreciated browser | Version 11.900.18362.0 |
| Brave            | PC         | Excellent                                                    | Version 1.10.93        |
| Samsung Internet | Galaxy S8  | Excellent                                                    | Version 11.2.2.3       |
| Safari           | iPhone 8   | Excellent                                                    | Version 13.1           |

- [x] Test links to all pages
- [x] Test errors by typing in random page redirects
- [x] Try to access the user area without signing in
- [x] Test filtering dropdowns
- [x] Test searching
- [x] Test clear search
- [x] Tests card reveals
- [x] Test social links
- [x] Test recipe rating system
- [x] Test recipe share links
- [x] Test print option
- [x] Test account registration
- [x] Test add to favourites 
- [x] Test remove from favourites
- [x] Test update profile picture
- [x] Test update profile info
- [x] Test create recipe forms
- [x] Test add / del ingredients
- [x] Test add recipe image
- [x] Test delete recipe 
- [x] Test sign out 
- [x] Test sign in
- [x] Test delete profile 

#### User Testing

This was probably the most useful of all, I had a number of friends and family test the application. This helped me get feedback and find bugs I had missed. some included styling issues on different devices to some UX ideas to make it a bit more intuitive. Unfortunately I could not implement all the suggested features in time but the feedback was invaluable.  Below are some of the feedback images I received and consequently fixed.

<img src="https://res.cloudinary.com/dajuujhvs/image/upload/v1592642702/homechopped/user_tests_xl6tsr.png" style="zoom:50%;" alt=" user feedback image" />



------



### Deployment

The repository for this project is hosted on [GitHub](https://github.com/) and uses [Heroku](https://www.heroku.com/) to serve the site to the world. If you would like to contribute to this project or run it locally you would need to first have some sort of code editor installed like [VS Code](https://code.visualstudio.com/) and some version control software like [Git](https://git-scm.com/), you will also need a GitHub account.

#### Prerequisites

In order to contribute to this repository you will need to have the following installed:

- Python 3.8.3 or higher
- Git version control
- Code editor - [Pycharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/)  is recommended

#### Development

There are a number of steps required to deploy a local version of this project. 

##### Cloning

- At the top of the repository click on the `Clone or download button`
- Copy the path to the repo `https://github.com/Frozenaught/homechopped.git`
- In your command-line, navigate to the folder where you would like to make a copy of this repository -`c:\MyRepos> `.
- Type the following to clone the repo `c:\MyRepos> git clone https://github.com/Frozenaught/homechopped.git`
- Now you can navigate to the newly created directory `c:\MyRepos\homechopped>`

##### Requirements

Next you will need to install all the projects dependencies type `pip install -r requirements.txt`. If you add or update any new packages to the project use `pip freeze --local > requirements.txt ` to update the [requirements.txt](requirements.txt) file with the new dependencies.

##### Environment Variables

You will need to setup the following environment variables on your system.

| Variable name         | Used for                 | Notes                                                        |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| CLOUDINARY_CLOUD_NAME | Cloudinary Image package | Found in your Clouinary account dashboard                    |
| CLOUDINARY_API_KEY    | Cloudinary Image package | Found in your Clouinary account dashboard                    |
| CLOUDINARY_API_SECRET | Cloudinary Image package | Found in your Clouinary account dashboard                    |
| HC_MONGO_DBNAME       | Mongo DB                 | This is the name of your database collection eg: `homechoped` |
| HC_MONGO_URI          | Mongo DB                 | Found in the connect button on the database cluster          |
| SESSION_SECRET        | Session Variables        | This is a unique secret used for cookie encryption,  you can use any random string for this |
| IP                    | Flask                    | You can use `0.0.0.0` here to indicate a local IP address    |
| PORT                  | Flask                    | You can use the default port `5000`                          |



> Note: you will need to add these environment variable to your GitHub repo in `settings -> secrets` and Heroku  in `settings -> config vars` 

##### Contribution

- If you chose to make changes to the website I would recommend using separate branches so that you can go back to the original master branch if the changes don't work as expected.
- Use `git checkout -b <brancname>` to create a new branch and edit the files accordingly.
- If you are happy with the changes to use `git commit -m "my commit message of changes I have made"` to commit the changes.
- Use `git push `to push the changes to the repository.
- As these changes are on a different branch they will not be available on the deployed site until you merge them to the master branch.
- To merge the new branch to the master branch switch to the new branch on GitHub using the branch selector dropdown menu.
- create a new pull request and state what changes were made in the comment section.
- submit the pull request and switch back to the master branch.
- now you will have the option to merge the pull request and you will be done.

##### Deployment

The easiest way to deploy the project to Heroku is to set your connect method to GitHub and link the repository master branch. If you set the project up for automatic deploys it will deploy once the master branch is updated.

------

## Credits

The bulk of the credits should really go to the documentation of the various technologist I used, I managed to get most of what I needed from there.

### Content

The recipes on the site are all real recipes taken from [BBC Food](https://www.bbc.co.uk/food), all the text was copied from the links in [this trello card](https://trello.com/c/cSwtE1RE/71-recipes)

### Media

#### Images

- Placeholder images - [Icon Library](http://icon-library.com/)
- Placeholder profile picture - [PNG Item](https://www.pngitem.com/)
- Error Images - [Drlinkcheck](https://www.drlinkcheck.com/blog/free-http-error-images)
- Recipe images - [Pixabay](https://pixabay.com/)

#### Name

- The name was generated using - [Biz name wiz](https://biznamewiz.com/)

### Acknowledgements

Along the development process I saved all references I used to the References area in my [Trello Board](https://trello.com/b/8o2Zv6LB/ci-milestone-3-homechopped)

#### Inspiration

- used to help with ideas for web design
  - [Food Gawker](https://foodgawker.com/post/category/beef/)
  - [BBC Food](https://www.bbc.co.uk/food)

#### Code

- Help with login system - [Login System](https://www.youtube.com/watch?v=vVx1737auSE)
- Cloudinary image upload 
  - [Image Widgets](https://cloudinary.com/documentation/upload_widget#create_upload_widget_methods)
  - [Sample Repo](https://github.com/cloudinary/pycloudinary/blob/master/samples/basic/basic.py)
- [Rate system](https://www.cssscript.com/five-star-rating-system-with-pure-css-and-radio-button-hack/)
- [Print Button](https://www.thoughtco.com/how-to-add-a-print-button-4072006)
- [Social links](https://css-tricks.com/simple-social-sharing-links/)
- [Project structure](https://pythonise.com/series/learning-flask/flask-application-structure)
- General queries [Stack overflow](https://stackoverflow.com/)