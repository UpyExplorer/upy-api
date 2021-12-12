import os
import environ
from flask_swagger_ui import get_swaggerui_blueprint

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

FLASK_ENV = env("FLASK_ENV")

if FLASK_ENV == 'production':
    from app.conf.production.settings import *
else:
    from app.conf.development.settings import *

SWAGGER_URL = '/docs'
API_URL = BASE_DIR + "/staticfiles/swagger.json"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "UpyExplorer"
    }
)