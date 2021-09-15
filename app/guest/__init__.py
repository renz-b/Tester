from flask import Blueprint

guest = Blueprint('guest', __name__)

from . import views