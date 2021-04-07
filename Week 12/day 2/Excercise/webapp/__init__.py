# Use python to create a random secret key composed of 256 random letters.

import flask

import random
import string

app = flask.Flask(__name__)


from config import Config

app.config.from_object(Config)


