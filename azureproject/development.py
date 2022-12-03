"""
development.py -    Script that is run when the code is deployed on a development level
"""
from pathlib import Path
import os

from flask.cli import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env_file_name = ".env"
env_path = Path.cwd().parent.joinpath(f"{env_file_name}")
load_dotenv(env_path)
print(env_path)

DEBUG = True

load_dotenv()
DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'

