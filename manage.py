#!/usr/bin/env python
import os
import sys
import imp


from migrate.versioning import api

from settings import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app import xanadu, db

COMMANDS = {
    'runserver',
    'tests',
    'createdb',
    'upgradedb',
    'downgradedb',
    'dbversion',
    'migrate',
}


def runserver():
    '''
    runs the flask server on localhost:5000
    '''
    xanadu.run(debug=True)


def get_db_version():
    return api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)


def downgrade_db(num=1):
    '''
    downgrade the version of the db to the desired revision
    '''
    version = get_db_version()
    api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                  version-num)  # downgrade the version num number of times
    version = get_db_version()
    print('Current database version: ' + str(version))


def upgrade_db():
    '''
    upgrade the version of the database with the current version
    '''
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    version = get_db_version()
    print('Current database version: ' + str(version))


def migrate():
    '''
    make migrations and save them in migrations file
    '''
    version = get_db_version()
    migration = SQLALCHEMY_MIGRATE_REPO +\
        ('/versions/{:03}_migration.py'.format(version+1))
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(
        SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    exec(old_model, tmp_module.__dict__)
    script = api.make_update_script_for_model(
        SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
        tmp_module.meta, db.metadata)
    open(migration, "wt").write(script)
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    version = get_db_version()
    print('New migration saved as ' + migration)
    print('Current database version: ' + str(version))


def create_db():
    '''
    Create the database
    '''
    db.create_all()
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'migrations')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(
            SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
            api.version(SQLALCHEMY_MIGRATE_REPO))


if __name__ == '__main__':
    no_of_arguments = len(sys.argv)
    if no_of_arguments > 1:
        if sys.argv[1].lower() in COMMANDS:
            command = sys.argv[1].lower()
            if command == 'runserver':
                runserver()
            if command == 'createdb':
                create_db()
            if command == 'upgradedb':
                upgrade_db()
            if command == 'downgradedb':
                try:
                    if no_of_arguments == 3 and int(sys.argv[2]):
                        downgrade_db(num=int(sys.argv[2]))
                    elif no_of_arguments == 2:
                        downgrade_db()
                except:
                    raise ValueError(
                        'Number of versions to downgrade should be an integer'
                        )
            if command == 'dbversion':
                print(str(get_db_version()))
            if command == 'migrate':
                migrate()
        else:
            raise ValueError('Invalid Command!')
    else:
        raise ValueError('No command to run specified!!')
