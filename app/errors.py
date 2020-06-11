from app import app
from flask import render_template

'''404 Not Found
The good old “chap, you made a mistake typing that URL” message. So common that even novices to the internet know that 404 means: damn, the thing I was looking for is not there. It’s a very good idea to make sure there is actually something useful on a 404 page, at least a link back to the index.

403 Forbidden
If you have some kind of access control on your website, you will have to send a 403 code for disallowed resources. So make sure the user is not lost when they try to access a forbidden resource.

410 Gone
Did you know that there the “404 Not Found” has a brother named “410 Gone”? Few people actually implement that, but the idea is that resources that previously existed and got deleted answer with 410 instead of 404. If you are not deleting documents permanently from the database but just mark them as deleted, do the user a favour and use the 410 code instead and display a message that what they were looking for was deleted for all eternity.

500 Internal Server Error
Usually happens on programming errors or if the server is overloaded. A terribly good idea is to have a nice page there, because your application will fail sooner or later (see also: Application Errors).'''


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(403)
def page_not_found(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 403 status explicitly
    return render_template('500.html'), 500
