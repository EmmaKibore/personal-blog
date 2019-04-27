<<<<<<< HEAD
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_mail import Mail

=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from .auth import auth as auth_blueprint
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_mail import Mail
from config import config_options
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
<<<<<<< HEAD
mail = Mail()

bootstrap = Bootstrap()

db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    bootstrap = Bootstrap(app)
    login_manager.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # registering the main app blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
=======

bootstrap = Bootstrap()
mail = Mail()
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)
simple = SimpleMDE()
simple.init_app(app)

photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #creating the app configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    #registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709

    # configure UploadSet
    configure_uploads(app,photos)

<<<<<<< HEAD
    return app 
=======
    return app
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
