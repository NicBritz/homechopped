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