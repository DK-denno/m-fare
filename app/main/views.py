from . import main
from flask import render_template
from .. import db
from .request import Api_call

@main.route('/',methods=['GET','POST'])

def index():
    api_call = Api_call()
    
    return render_template('index.html',api_call=api_call)