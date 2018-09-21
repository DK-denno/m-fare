from . import db
from flask_login import UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash
# import login manager
from . import login_manager

class Admin(UserMixin, db.Model):
    """
    creating class writer for creating blog writer and connecting it to database via db.Model

    """
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # call  back function retrieving writer id
    @login_manager.user_loader
    def load_user(admin_id):
        return Admin.query.get(int(admin_id))

    def set_password(self, password):
        """
        method to set passwords
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        method to verify password
        """
        return check_password_hash(self.pass_secure, password)

class Roles(UserMixin, db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(255))
    user = db.relationship('User',backref='users',lazy="dynamic")
    sacco = db.relationship('Sacco',backref='sacco',lazy="dynamic")



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    username = db.Column(db.String(255), index=True)
    password_secure = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    role = db.Column(db.Integer,db.ForeignKey('roles.id'))

    # call  back function retrieving writer id
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

   
    def save_user(self):
       db.session.add(self)
       db.session.commit()

    def delete_user(cls,id):
       db.session.delete(id)
       db.session.commit()

    @property
    def password(self):
       raise AttributeError('YOU CANNOT ACCESS THIS DETAILS')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
       return check_password_hash(self.password_secure,password)


class Sacco(UserMixin,db.Model):

    __tablename__ = 'sacco'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index = True)
    sacconame = db.Column(db.String(255),index = True)
    password_secure = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    route = db.Column(db.String(10000))
    roles_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    fares = db.relationship('Fares',backref='faress',lazy="dynamic")



    def save_sacco(self):
       db.session.add(self)
       db.session.commit()

    def delete_sacco(cls,id):
       db.session.delete(id)
       db.session.commit()


    def get_routes(sacconame):
        sacco = Sacco.query.filter_by(sacconame = sacconame).first()
        return sacco


    @property
    def password(self):
       raise AttributeError('YOU CANNOT ACCESS THIS DETAILS')

    @password.setter
    def password(self,password):
       self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
       return check_password_hash(self.password_secure,password)

class Fares(db.Model):
    __tablename__ = 'fares'

    id = db.Column(db.Integer, primary_key=True)
    fare = db.Column(db.Integer)
    sacco_id = db.Column(db.ForeignKey('sacco.id'))

    def save_fare(self):
       db.session.add(self)
       db.session.commit()
