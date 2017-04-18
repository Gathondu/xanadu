#!/usr/bin/env python
import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from xanadu import create_app, db
from xanadu.models import user, bucketlist, item


xanadu = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(xanadu)

# database migration logic added to manager
migrate = Migrate(xanadu, db)


# shell commands logic
def make_shell_context():
    """Add imports that will be existent in the shell"""
    return dict(
        xanadu=xanadu, db=db, User=user.User, BucketList=bucketlist.BucketList, Item=item.Item)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

COV = None
if os.getenv('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, source=['xanadu'], omit=['*/tests/*'])
    COV.start()


@manager.command
def tests(coverage=False):
    """run the unit tests with option of including coverage"""
    if coverage and not os.getenv('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=1).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://{}/index.html'.format(covdir))
        COV.erase()


@manager.command
def dropdb():
    """drop the database"""
    db.reflect()
    db.drop_all()


@manager.command
def deploy():
    """run deployment tasks"""
    from flask_migrate import upgrade

    upgrade()

if __name__ == '__main__':
    manager.run()
