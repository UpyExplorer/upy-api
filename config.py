import os
from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
DEBUG = os.environ.get("DEBUG")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "UpyExplorer"
    }
)