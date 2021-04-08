# Use python to create a random secret key composed of 256 random letters.

import flask

import random
import string
from config import Config

app = flask.Flask(__name__)

app.config.from_object(Config)

from . import routes

