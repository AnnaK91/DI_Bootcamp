import flask

app = flask.Flask(__name__)


@app.route("/home")

def home():
    return flask.render_template("task.html")




@app.route("/red")
def color():
    return flask.render_template("red.html")

app.run(port=5001, debug = True)
