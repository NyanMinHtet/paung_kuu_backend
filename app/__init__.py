from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    # ensure models are imported so migrations discover them
    import app.models  # noqa: F401 (module import side-effects)
    migrate.init_app(app, db)

    from app.api.users import users_blueprint
    from app.api.auth import auth_blueprint

    app.register_blueprint(users_blueprint, url_prefix='/api')
    app.register_blueprint(auth_blueprint, url_prefix='/api')

    return app