from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movies_ns


def create_app(config_object) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())
app.debug = True
migrate = Migrate(app, db, render_as_batch=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
