#__init__ user_auth
from flask import Blueprint

user_auth = Blueprint('user_auth',__name__)

from . import views,forms



