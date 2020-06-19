from app import app


################
# PROFILE VIEW #
################
def test_profile():
    # test page link
    response = app.test_client().get('/profile', follow_redirects=True)
    assert response.status_code == 200
    # test error handeling
    response = app.test_client().get('/profile/fsaryfd')
    assert response.status_code == 404


#####################
# EDIT PROFILE VIEW #
#####################
def test_edit_profile():
    # test page link
    response = app.test_client().get('/edit_profile/', follow_redirects=True)
    assert response.status_code == 404
    # test error handeling
    response = app.test_client().get('/edit_profile/fsghhhj', follow_redirects=True)
    assert response.status_code == 404


##################
# UPDATE PROFILE #
##################
def test_update_profile():
    # test page link
    response = app.test_client().get('/update-profile/', follow_redirects=True)
    assert response.status_code == 404
    # test error handeling bad server request
    response = app.test_client().post('/update-profile/sdfsdf', data={'bio': 'asdfsdfsd'}, follow_redirects=True)
    assert response.status_code == 500


##################
# DELETE PROFILE #
##################
def test_delete_user():
    # test page link
    response = app.test_client().get('/delete-user/', follow_redirects=True)
    assert response.status_code == 404
    # test forbidden
    response = app.test_client().get('/delete-user/dfsgss', follow_redirects=True)
    assert response.status_code == 403


#################
# ADD FAVORITE  #
#################
def test_add_favorite():
    # test page link
    response = app.test_client().get('/add_favorite/', follow_redirects=True)
    assert response.status_code == 404
    # test error handeling
    response = app.test_client().get('/add_favorite/hfdghfgdf', follow_redirects=True)
    assert response.status_code == 404


####################
# REMOVE FAVORITE  #
####################
def test_remove_favorite():
    # test page link
    response = app.test_client().get('/remove_favorite/', follow_redirects=True)
    assert response.status_code == 404
    # test error handeling
    response = app.test_client().get('/remove_favorite/sfrrsf', follow_redirects=True)
    assert response.status_code == 404
