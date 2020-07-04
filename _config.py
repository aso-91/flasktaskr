from pathlib import Path, PurePath

import os

# grab the folder where this script lives
basedir = PurePath(__file__).parent
# basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'


# define the full path for the database
# DATABASE_PATH = os.path.join(basedir, DATABASE)
DATABASE_PATH = basedir.joinpath(DATABASE)