'''
controllers for errors
'''
from flask import render_template
from . import main


# use main.app_errorhandler for application wide error handling
# main.errorhandler only invokes errors defined in the blueprint
@main.app_errorhandler(404)
def page_not_found(error):
    '''render page not found errors'''
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(error):
    '''render server errors'''
    return render_template('500.html'), 500
