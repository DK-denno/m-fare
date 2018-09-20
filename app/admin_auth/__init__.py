from flask import Blueprint

# creating a blueprint instance
admin_auth = Blueprint('admin_auth', __name__)

from . import views, forms