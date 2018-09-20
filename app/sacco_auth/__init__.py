from flask import Blueprint

sacco_auth = Blueprint('sacco_auth',__name__)

from . import views,forms