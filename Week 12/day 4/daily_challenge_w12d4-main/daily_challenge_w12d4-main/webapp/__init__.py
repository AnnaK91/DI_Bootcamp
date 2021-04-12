import os

import flask
import flask_sqlalchemy, flask_migrate


app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "thisisaverysecretKEY"


# __file__ is __init__.py --> Here it's special bc __init__.py is actually webapp/
# >>> __file__ is webapp/ <<<
# os.path.dirname(path) is the name of the parent directory of the path
# >>> os.path.dirname("webapp") is daily_challenge_w12d3 <<<
# os.path.abspath(path) is the absolute path to path
# >>> os.path.abspath("daily_challenge_w12d3") is /home/eyal/..../daily_challenge_w12d3 <<<

# --> At the end, basedir is the aboslute path of the project folder

basedir = os.path.abspath(os.path.dirname(__file__)) # import os !

os.path.join(basedir, "webapp/myfile.json")
"./webapp/static"

# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Poggero1991@localhost:5432/airline"

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app=app, db=db)


from . import models, routes


def load_users_json():
    """
    Return a list of users dictionaries
    """
    filename = os.path.join(basedir, "webapp/static/users.json")

    f = open(filename, 'r')
    users = json.load(f)
    f.close()

    return users

def populate(db):
    users = load_users_json()

    for user in users:
        # Create user
        user_obj = models.User(
            name = user["name"],
            street = user["address"]["street"],
            city = user["address"]["city"],
            zipcode = user["address"]["zipcode"],
        )

        # Add it to the database
        db.session.add(user_obj)
        db.session.commit()

        print(f"Added {user_obj['name']} to the DB !")


populate(db)