from flask import Flask
from config import config_options, Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from AfricasTalkingGateway import AfricasTalkingGateway,AfricasTalkingGatewayException

africastalkinggateway = AfricasTalkingGateway()
africastalkinggatewayexception = AfricasTalkingGatewayException()
migrate = Migrate()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)

    #initialising flask extensions
    bootstrap.init_app(app)
    africastalkinggatewayexception.init_app(app)
    africastalkinggateway.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app
