#!/usr/bin/env python
import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from xanadu import create_app, db
from xanadu.models import User, Item


xanadu = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(xanadu)

# database migration logic added to manager
migrate = Migrate(xanadu, db)


# shell commands logic
def make_shell_context():
    '''Add imports that will be existent in the shell'''
    return dict(xanadu=xanadu, db=db, User=User, Item=Item)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def tests():
    '''run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def dropdb():
    '''drop the database'''
    db.drop_all()

if __name__ == '__main__':
    manager.run()
