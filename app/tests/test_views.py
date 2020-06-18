from app import app


##############
# INDEX VIEW #
##############

def test_index_main():
    # test page link
    response = app.test_client().get('/')
    assert response.status_code == 200
    # test pages,limits and page number
    response = app.test_client().get('/1/2/1')
    assert response.status_code == 200
    # test error handling
    response = app.test_client().get('/sgad1')
    assert response.status_code == 404


######################
# INDEX LIMIT AMOUNT #
######################

def test_index_limit():
    # test redirect limit
    response = app.test_client().post('/index_limit/', data={'amount': '8'})
    assert response.status_code == 302
    # valid respose from index view
    response = app.test_client().post('/index_limit/', data={'amount': '8'}, follow_redirects=True)
    assert response.status_code == 200
    # ivalid
    response = app.test_client().post('/index_limit/', data={'amount': 'a'}, follow_redirects=True)
    assert response.status_code == 404


##############
# INDEX SORT #
##############
def test_index_sort():
    # test redirect sort
    response = app.test_client().post('/index_sort/1/2', data={'sort': '1'})
    assert response.status_code == 308
    # valid respose from index view
    response = app.test_client().post('/index_sort/1/2', data={'sort': '1'}, follow_redirects=True)
    assert response.status_code == 200
    # ivalid respose from index view
    response = app.test_client().post('/index_sort/1/2', data={'sort': 'a'}, follow_redirects=True)
    assert response.status_code == 404


#################
# FEATURED VIEW #
#################

def test_featured_main():
    # test page link
    response = app.test_client().get('/featured/')
    assert response.status_code == 200
    # test pages,limits and page number
    response = app.test_client().get('/featured/1/2/1')
    assert response.status_code == 200
    # test error handling
    response = app.test_client().get('/featured/sgad1')
    assert response.status_code == 404


#########################
# FEATURED LIMIT AMOUNT #
#########################

def test_featured_limit():
    # test redirect limit
    response = app.test_client().post('/featured_limit/', data={'amount': '2'})
    assert response.status_code == 302
    # valid respose from index view
    response = app.test_client().post('/featured_limit/', data={'amount': '2'}, follow_redirects=True)
    assert response.status_code == 200
    # ivalid
    response = app.test_client().post('/featured_limit/', data={'amount': 'a'}, follow_redirects=True)
    assert response.status_code == 404


#################
# FEATURED SORT #
#################
def test_featured_sort():
    # test redirect sort
    response = app.test_client().post('/featured_sort/1/2', data={'sort': '1'})
    assert response.status_code == 308
    # valid respose from index view
    response = app.test_client().post('/featured_sort/1/2', data={'sort': '1'}, follow_redirects=True)
    assert response.status_code == 200
    # ivalid respose from index view
    response = app.test_client().post('/featured_sort/1/2', data={'sort': 'a'}, follow_redirects=True)
    assert response.status_code == 404



############
# ALL VIEW #
############

def test_all_recipes_main():
    # test page link
    response = app.test_client().get('/all_recipes/')
    assert response.status_code == 200
    # test pages,limits and page number
    response = app.test_client().get('/all_recipes/1/2/1')
    assert response.status_code == 200
    # test error handling
    response = app.test_client().get('/all_recipes/sgad1')
    assert response.status_code == 404


####################
# ALL LIMIT AMOUNT #
####################

def test_all_recipes_limit():
    # test redirect limit
    response = app.test_client().post('/all_recipes_limit/', data={'amount': '2'})
    assert response.status_code == 302
    # valid respose from index view
    response = app.test_client().post('/all_recipes_limit/', data={'amount': '2'}, follow_redirects=True)
    assert response.status_code == 200
    # ivalid
    response = app.test_client().post('/all_recipes_limit/', data={'amount': 'a'}, follow_redirects=True)
    assert response.status_code == 404


############
# ALL SORT #
############
def test_all_recipes_sort():
    # test redirect sort
    response = app.test_client().post('/all_recipes_sort/1/2', data={'sort': '1'})
    assert response.status_code == 308
    # valid respose from index view
    response = app.test_client().post('/all_recipes_sort/1/2', data={'sort': '1'}, follow_redirects=True)
    assert response.status_code == 200
    # ivalid respose from index view
    response = app.test_client().post('/all_recipes_sort/1/2', data={'sort': 'a'}, follow_redirects=True)
    assert response.status_code == 404

##############
# SEARCH VIEW#
##############

def test_search_recipes_main():
    # test page link
    response = app.test_client().get('/search_recipes/')
    assert response.status_code == 200
    # test pages,limits and page number
    response = app.test_client().get('/search_recipes/1/2/1')
    assert response.status_code == 404
    # test error handling
    response = app.test_client().get('/search_recipes/sgad1')
    assert response.status_code == 404
    response = app.test_client().post('/search_recipes/', data={'search': 'chicken'})
    assert response.status_code == 200