from app import app

###############
# RECIPE VIEW #
###############

def test_recipe_main():
    # test page link
    response = app.test_client().get('/recipe/')
    assert response.status_code == 404
    # test pages,limits and page number
    response = app.test_client().get('/recipe/5ee8f301c6eaae959bac7b00')
    assert response.status_code == 200
    # test error handling
    response = app.test_client().get('/recipe/sgad1')
    assert response.status_code == 404


###############
# TEMP RECIPE #
###############

def test_temp_recipe():
    # test page link
    response = app.test_client().get('/add_temp_recipe/')
    assert response.status_code == 404
    # test redirect
    response = app.test_client().get('/add_temp_recipe/gfdsgd', follow_redirects=True)
    assert response.status_code == 200


####################
# EDIT RECIPE VIEW #
####################

def test_edit_recipe():
    # test page link
    response = app.test_client().get('/edit_recipe/')
    assert response.status_code == 404
    # test error checking
    response = app.test_client().get('/edit_recipe/gfdsgd/sfdds', follow_redirects=True)
    assert response.status_code == 200


#################
# UPDATE RECIPE #
#################

def test_update_recipe():
    # test page link
    response = app.test_client().get('/update_recipe/')
    assert response.status_code == 404
    # test error checking
    response = app.test_client().get('/update_recipe/gfdsgd/asfas', follow_redirects=True)
    assert response.status_code == 404


#######################
# UPDATE RECIPE IMAGE #
#######################

def test_update_recipe_image():
    # test page link
    response = app.test_client().get('/update_recipe_image/')
    assert response.status_code == 404
    # test error checking
    response = app.test_client().get('/update_recipe_image/gfdsgd/asfas', follow_redirects=True)
    assert response.status_code == 404


#################
# DELETE RECIPE #
#################

def test_delete_recipe():
    # test page link
    response = app.test_client().get('/delete_recipe/')
    assert response.status_code == 404
    # test redirect
    response = app.test_client().get('/delete_recipe/gfdsgd', follow_redirects=True)
    assert response.status_code == 200


##################
# ADD INGREDIENT #
##################
def test_add_ingredient_item():
    # test page link
    response = app.test_client().get('/add_ingredient_item/')
    assert response.status_code == 404
    # test error
    response = app.test_client().get('/add_ingredient_item/gfdsgd/sfsdf', follow_redirects=True)
    assert response.status_code == 404


#####################
# DELETE INGREDIENT #
#####################
def test_delete_ingredient_item():
    # test page link
    response = app.test_client().get('/delete_ingredient_item/')
    assert response.status_code == 404
    # test error
    response = app.test_client().get('/adelete_ingredient_item/gfdsgd/sfsdf', follow_redirects=True)
    assert response.status_code == 404


###################
# ADD METHOD ITEM #
###################
def test_add_method_item():
    # test page link
    response = app.test_client().get('/add_method_item/')
    assert response.status_code == 404
    # test error
    response = app.test_client().get('/add_method_item/gfdsgd/sfsdf', follow_redirects=True)
    assert response.status_code == 404


######################
# DELETE METHOD ITEM #
######################
def test_delete_method_item():
    # test page link
    response = app.test_client().get('/delete_method_item/')
    assert response.status_code == 404
    # test error
    response = app.test_client().get('/delete_method_item/gfdsgd/sfsdf', follow_redirects=True)
    assert response.status_code == 404


###############
# RATE RECIPE #
###############
def test_rate_recipe():
    # test page link
    response = app.test_client().get('/rate_recipe/')
    assert response.status_code == 404
    # test post
    response = app.test_client().post('/rate_recipe/ghfjgf', data={'rating': '1'}, follow_redirects=True)
    assert response.status_code == 404
