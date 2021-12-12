import os
import environ
from os.path import dirname

BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

print(BASE_DIR+"/.env")

DEBUG = env.bool("DEBUG", False)
PORT = env("PORT")
HOST = env("HOST")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI")

DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = env("CSRF_SESSION_KEY")
SECRET_KEY = env("SECRET_KEY")
