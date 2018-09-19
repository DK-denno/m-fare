from . import db
from flask_login import UserMixin, login_user
from werkzeug.security import generate_password_hash,check_password_hash

class Roles(UserMixin,db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.String(255))
    user = db.relationship('User',backref='users',lazy="dynamic")


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index = True)
    username = db.Column(db.String(255),index = True)
    password_secure = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    role = db.Column(db.String(255),db.ForeignKey('roles.role'))


    @classmethod
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
    def password(self,password):
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
    route = db.Column(db.String(255))
    fares = db.relationship('Fares',backref='fare',lazy="dynamic")

    @classmethod
    def save_sacco(self):
        db.session.add(self)
        db.session.commit()

    def delete_sacco(cls,id):
        db.session.delete(id)
        db.session.commit()


    @property
    def password(self):
        raise AttributeError('YOU CANNOT ACCESS THIS DETAILS')

    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
class Fares(db.Model):
    __tablename__='fares'
    id = db.Column(db.Integer,primary_key=True)
    fare = db.Column(db.Integer)
    sacco_id = db.Column(db.ForeignKey('sacco.id'))

        
