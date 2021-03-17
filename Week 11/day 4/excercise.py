# Create a view that displays a greeting message. The greeting message should change depending on the time of day the url to this view is accessed.
# Between 08:00 and 13:00 the message should display - Good Morning.
# Between 13:00 and 17:00 the message should display - Good Afternoon.
# Between 17:00 and 21:00 the message should display - Good Evening.
# Between 21:00 and 08:00 the message should display - Good Night.

import flask
import datetime

app = flask.Flask(__name__)


@app.route("/greetings")

def greetings():

    d = datetime.datetime.now()

    return flask.render_template("greetings.html", date_obj=d)


app.run(port=5001, debug = True)