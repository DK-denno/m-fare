from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
<<<<<<< HEAD
<<<<<<< HEAD
from app.models import User, Sacco, Fares, Roles
=======
from app.models import Admin,User,Sacco,Fares
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee
=======
from app.models import Admin,User,Sacco,Fares
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee

app = create_app('development')
# app = create_app('test')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)


migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
<<<<<<< HEAD
<<<<<<< HEAD
    return dict(app=app, db=db, User=User, Sacco = Sacco, Fares = Fares, Roles = Roles)
=======
    return dict(app=app, db=db,Admin=Admin, User=User,Fares=Fares,Sacco=Sacco)
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee
=======
    return dict(app=app, db=db,Admin=Admin, User=User,Fares=Fares,Sacco=Sacco)
>>>>>>> 45084bb09f27ced6d6ae9e0526d807e29b88f6ee


if __name__ == '__main__':
    manager.run()
