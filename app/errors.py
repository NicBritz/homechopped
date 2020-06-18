from flask import render_template

from app import app


#############
# 403 ERROR #
#############
@app.errorhandler(403)
def page_forbidden(e):
    """ Redirects to the error template
    :returns
        403 FORBIDDEN template page
    """
    return render_template('403.html'), 403


#############
# 404 ERROR #
#############
@app.errorhandler(404)
def page_not_found(e):
    """ Redirects to the error template
    :returns
        404  NOT FOUND template page
    """
    return render_template('404.html'), 404


#############
# 410 ERROR #
#############
@app.errorhandler(410)
def page_gone(e):
    """ Redirects to the error template
    :returns
        410 GONE template page
    """
    return render_template('410.html'), 410


#############
# 500 ERROR #
#############
@app.errorhandler(500)
def server_error(e):
    """ Redirects to the error template
    :returns
        500 INTERNAL SERVER ERROR template page
    """
    return render_template('500.html'), 500
