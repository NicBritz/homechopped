from app import app

###########
# SIGN IN #
###########

def test_signin_main():
    # test page link
    response = app.test_client().get('/sign-in/')
    assert response.status_code == 200
    # test failure
    response = app.test_client().get('/sign-in/1/2/1')
    assert response.status_code == 404
    # test error handling
    response = app.test_client().get('/sign-in/sgad1')
    assert response.status_code == 404

############
# Register #
############

def test_register_main():
    # test page link
    response = app.test_client().get('/register/')
    assert response.status_code == 200
    # test failure
    response = app.test_client().get('/register/1/2/1')
    assert response.status_code == 404
    # test error handling
    response = app.test_client().get('/register/sgad1')
    assert response.status_code == 404