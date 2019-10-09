from flask import Flask
from flask_pymongo import PyMongo
import os

mongo = PyMongo()

class Config:
    '''Config object'''
    SECRET_KEY = 'omnistack'
    MONGO_URI = 'mongodb+srv://omnistack:omnistack@omnistack9-nqvfe.mongodb.net/flask_backend?retryWrites=true&w=majority'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/uploads')


def create_app(config_class=Config):
    '''Factory function'''
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)

    from app.controller.routes import routes
    from app.models import models
    app.register_blueprint(routes)
    app.register_blueprint(models)

    return app

