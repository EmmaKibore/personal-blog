from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .auth import auth as auth_blueprint
from flask import loginManager
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://emmah:kHAOYAISDEAD2008@localhost/test'
    db = SQLAlchemy(app)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)



    return app
