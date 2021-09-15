from flask_login import current_user
from flask import abort
from functools import wraps

def admin_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not current_user.is_administrator():
            abort(403)
        return function(*args, **kwargs)
    return decorated_function
