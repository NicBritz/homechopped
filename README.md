

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
├── __init__.py
├── errors.py
├── recipe.py
├── setup.py
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
├── test_views.py
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

## 

## Testing

Testing and error checking was undertaken throughout the development process. With the aid of the following tools and the help of human testers, I was able to catch and fix errors and bugs in my code.

#### [W3C Markup](https://validator.w3.org/)

Even though using this validator would understandably show errors for the jinja code i managed to catch some small mistakes by validating all the individual html files.

####  [W3C CSS](https://jigsaw.w3.org/css-validator/)

I tested all the CSS files in the project using W3C CSS validator with no errors as per image below.

![](https://res.cloudinary.com/dajuujhvs/image/upload/v1592421296/homechopped/valid_s0xh6m.png)

#### [Autoprefixer](https://autoprefixer.github.io/)

After finishing up my CSS and before the validation of CSS I used this tool to make sure I had not left out any prefixing in my code.

------

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X