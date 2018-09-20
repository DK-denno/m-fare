from . import main
from flask import render_template
from .. import db
from ..models import User
# from .request import Api_call

@main.route('/',methods=['GET','POST'])

def index():
   
    
    return render_template('index.html')



