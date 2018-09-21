from . import main
from flask import render_template
from .. import db
from ..models import User,Sacco
# from .request import Api_call

@main.route('/',methods=['GET','POST'])

def index():
   
    
    return render_template('index.html')

@main.route('/saccos',methods=['GET','POST'])
def saccos():
    saccos = Sacco.query.all()
    return render_template('sacco.html',saccos=saccos)


