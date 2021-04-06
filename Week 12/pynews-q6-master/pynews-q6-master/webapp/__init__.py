import flask
import flask_sqlalchemy
import flask_migrate

app = flask.Flask(__name__)

# In case you have: "A secret key is required to use..."
app.config["SECRET_KEY"] = "my-very-secret-key"
app.config['SQLALCHEMY_DATABASE_URI"] = "postgresql://Poggero1991@localhost/5432/pynews"
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate


# postgres = 

from . import routes, models

