import flask

app = flask.Flask(__name__)


@app.route("/home")

def home():
    return flask.render_template("task.html")




# @app.route("/blue")

# def blue():


app.run(port=5000, debug = True)


