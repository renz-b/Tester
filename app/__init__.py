from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
nav = Nav()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    nav.init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .guest import guest as guest_blueprint
    app.register_blueprint(guest_blueprint, url_prefix='/guest')

    login_nav = Navbar('Quick Test', 
        View('Login', 'auth.login'))
        
    nav.register_element('login_navbar', login_nav)

    return app
    