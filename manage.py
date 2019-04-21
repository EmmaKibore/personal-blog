from app import create_app,db
from app.models import User,Role,pitch
from flask_migrate import Migrate, MigrateCommand

app = create_app('production')

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User )

    migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
