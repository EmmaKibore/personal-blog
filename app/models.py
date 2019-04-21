from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.string(225)),index = True)
    email = db.Colunm(db.string(225),unique = True,index = True)
    role_id = db.Column(db.integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.string(225))
    profile_pic_path = db.Column(db.string())
    password_hash = db.Column(db.String(225))

        @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.model):
    __tablename__ = 'roles'


    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('Review',backref = 'user',lazy = "dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Review(db.Model):

    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

     def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews
