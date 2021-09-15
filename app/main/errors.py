from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
   message = "Page Not Found!"
   return render_template('errors/error.html', err_code=404, message=message)

@main.app_errorhandler(500)
def internal_server_error(e):
   message = "Internal Server Error!"
   return render_template('errors/error.html', err_code=500, message=message)
