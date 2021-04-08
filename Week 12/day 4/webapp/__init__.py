from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = flask.Flask(__name__)

app.config.from_object(Config)