from . import sacco_auth
from ..models import Sacco
from .forms import SaccoLoginForm,SaccoRegistrationForm
from .. import db
from flask_login import login_user,logout_user,login_required
from flask import render_template,redirect,url_for,flash,request


@sacco_auth.route('/login',methods=['GET','POST'])
def login():
    sacco_login_form = SaccoLoginForm()
    if sacco_login_form.validate_on_submit():
        sacco = Sacco.query.filter_by(email = sacco_login_form.email.data).first()
        if sacco is not None and sacco.verify_password(sacco_login_form.password.data):
            login_user(sacco,sacco_login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Email or Password')

    title = " login"
    return render_template('authentication/login.html',sacco_form = sacco_login_form,title=title)


@sacco_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))



@sacco_auth.route('/register',methods = ["GET","POST"])
def register():
    sacco_reg_form = SaccoRegistrationForm()
    if sacco_reg_form.validate_on_submit():
        saccos = Sacco(email = sacco_reg_form.email.data, sacconame = sacco_reg_form.sacconame.data,
                      password = sacco_reg_form.password.data, phone_number = sacco_reg_form.phone_number.data,
                      route = sacco_reg_form.route.data)

        saccos.save_sacco()
        return redirect(url_for('sacco_auth.dashboard',sacconame=saccos.sacconame))
    title = "New Sacco Account"
    return render_template('authentication/registration.html',sacco_reg_form = sacco_reg_form, title = title)

@sacco_auth.route('/sacco/dashboard/<sacconame>')
def dashboard(sacconame):
    '''
    Function to render the dashboad for saccos
    '''
    sacco = Sacco.query.filter_by(sacconame=sacconame).first()

    saccorote = (sacco.route).split(',')
    print(saccorote)
    saco = []
    for sac in saccorote:
        saco.append(sac)
    print(saco[1])
    return render_template('sacco/sacco_dashboard.html',sac=saco)

