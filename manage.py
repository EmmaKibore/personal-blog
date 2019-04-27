<<<<<<< HEAD
from app import create_app ,db
from flask_script import Manager,Server
from app.models import User, Comment, Post
from flask_migrate import Migrate , MigrateCommand

# app = create_app('production')
app = create_app('development')


manager = Manager(app)
manager.add_command('server',Server)
=======
from app import create_app,db
from app.models import User,Comment,Pitch
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server,Shell

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709

@manager.command
def test():
   """Run the unit tests."""
   import unittest
   tests = unittest.TestLoader().discover('tests')
   unittest.TextTestRunner(verbosity=2).run(tests)

<<<<<<< HEAD
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Comment = Comment, Post = Post )

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
   manager.run()
=======

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User,Pitch = Pitch, Comment = Comment )



if __name__ == '__main__':
    manager.run()
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
