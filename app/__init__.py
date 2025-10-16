import configparser
import os
from flask import Flask
from dotenv import load_dotenv
from .extensions import db, login_manager
from .login import auth_bp
from .main import main_bp
from pathlib import Path

load_dotenv()


def load_ini(fp):
    parser = configparser.ConfigParser()
    parser.read_file(fp)
    return dict(parser["flask"])


def create_app():
    app = Flask(__name__)

    base_dir = Path(__file__).parent.parent
    cfg_path = os.path.join(base_dir, "config.ini")
    app.config.from_file(cfg_path, load=lambda f: load_ini(f))

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        base_dir, os.environ.get("DATABASE_URL") or "").replace("\\", "/")

    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # type: ignore

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
