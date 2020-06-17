from flask import url_for
from app import app


##############
# INDEX VIEW #
##############

# test page root
def test_index_main():
    response = app.test_client().get('/')
    assert response.status_code == 200


# test pages,limits and page number
def test_index_pages():
    response = app.test_client().get('/1/2/1')
    assert response.status_code == 200


# test error handling
def test_index_error():
    response = app.test_client().get('/sgad1')
    assert response.status_code == 404


#################
# FEATURED VIEW #
#################

# test featured root
def test_featured_main():
    response = app.test_client().get('/featured/')
    assert response.status_code == 200
