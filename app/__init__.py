from flask import Flask, render_template
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from modules.public.api_doc.routes import mod_doc as doc

app.register_blueprint(app.config['SWAGGERUI_BLUEPRINT'], url_prefix=app.config['SWAGGER_URL'])
app.register_blueprint(doc)

db.init_app(app)
