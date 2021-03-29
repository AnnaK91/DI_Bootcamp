# Exercise 2
# Using Flask, create a template for your CV.
# Your CV should contain:
# Your name
# A picture
# Your hobbies
# Your skills
# Your strengths
# Your weaknesses
# Bonus: Add some CSS
# Hint : To add some CSS take a look at the video called Static Files in the Online Learning section.


import flask

app = flask.Flask(__name__)



@app.route("/home")
def homepage():

    return "Hello World"


@app.route("/resume")

def resume():
    return flask.render_template("CV.html")


app.run(port=5001, debug = True)