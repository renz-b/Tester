from flask import Blueprint, request

auth = Blueprint('auth', __name__)

from . import views
