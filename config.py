import os
import environ
from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

DEBUG = env("DEBUG")
PORT = env("PORT")
HOST = env("HOST")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI")
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = env("CSRF_SESSION_KEY")
SECRET_KEY = env("SECRET_KEY")

SWAGGER_URL = '/docs'
API_URL = BASE_DIR + "/staticfiles/swagger.json"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "UpyExplorer"
    }
)