from flask import Flask
from config import config_options, Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# from AfricasTalkingGateway import AfricasTalkingGateway,AfricasTalkingGatewayException

# africastalkinggateway = AfricasTalkingGateway()
# africastalkinggatewayexception = AfricasTalkingGatewayException()
migrate = Migrate()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_view = 'user_auth.login'


def create_app(config_name):
    app = Flask(__name__)

    #initialising flask extensions
    bootstrap.init_app(app)
    # africastalkinggatewayexception.init_app(app)
    # africastalkinggateway.init_app(app)
    db.init_app(app)
<<<<<<< HEAD


    login_manager.init_app(app)

    bootstrap.init_app(app)

    login_manager.init_app(app)
    migrate.init_app(app,db)

=======
    login_manager.init_app(app)
    migrate.init_app(app,db)
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

<<<<<<< HEAD

    from .sacco_auth import sacco_auth as sacco_blueprint
    app.register_blueprint(sacco_blueprint)

=======
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee
    from .admin_auth import admin_auth as admin_auth_blueprint
    app.register_blueprint(admin_auth_blueprint, url_prefix='/admin_auth')

    from .sacco_auth import sacco_auth as sacco_auth_blueprint
    app.register_blueprint(sacco_auth_blueprint,url_prefix='/sacco_auth')

    from .user_auth import user_auth as user_auth_blueprint
    app.register_blueprint(user_auth_blueprint,url_prefix = '/user_auth')
<<<<<<< HEAD

=======
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee
    
    from .urls import urls as urls_blueprint
    app.register_blueprint(urls_blueprint,url_prefix='/africas-talking')

    return app
