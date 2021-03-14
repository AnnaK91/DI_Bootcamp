import flask
import random

import requests     # "Module not found" --> pip install requests

url = "https://newsapi.org/v2/everything"
token = "5719809a4f814d0d9f8cb98e7a3d97de"

def get_news(query):
    params = {
        "apiKey": token,
        "q": "query",
        "from": "2021-03-01"
    }

    results = requests.get(url, params=params)
    return results.json()['articles']

print(get_news("python"))


#create a controller unsing flask.Flask class


app = flask.Flask(__name__)

# 127.0.0.1:5000/ 
# 127.0.0.1:5000/home

@app.route("/home") # --> will assign the function to www.yourdomain.com/home

def homepage():

    return "<html><body><h3> Hello world! </h3></body></html>"

#create a function so that when a user calls 

#127.0.0:5000/random-number
#He sees a random number between 1 and 100 on his screen


@app.route("/random-number")

def random_number():
    
    number = random.randint(1, 100)
    return f"Your number is {number}"

@app.route("/greet/<name>")
def greeting_message(name):
   # return f"Hello, {name}, nice to meet you!"
#create a template: greet.html
#add an h1 tag that says hello to the user

    return flask.render_template("greet.html", name=name)


@app.route("/news/<topic>")

def news(topic):
    # article = get_news(topic)[0]
    articles = get_news(topic) [:5]

    return flask.render_template("articles.html", articles=articles)



#Create one function: prettify_article(article)
#This function is receiving one article and returning and html code displaying in a pretty way

#Input:
#[{'source': {'id': 'reuters', 'name': 'Reuters'}, 
# 'author': 'Michael Church', 'title': 'Soccer is cool',
# 'description': "A very good article"
#}]
# def prettify_article(article):
#     return f"""
#         <div>
#             <p> {article['title']} </p>
#             <p> {article['description']} </p>
#             <small> {article['author']}</small>
#         </div>"""

# @app.route("/news/<keyword>")
# def news(keyword):
#     articles = get_news(keyword)[:5]
#     html = "<html>\n"
#     for article in articles:
#         html += prettify_article(article)

#     html += "</html>"
#     return html

# @app.route("/news/<topic>")
# def news(topic):
#     return flask.render_template("articles.html", name="Rick")




app.run(port=5001, debug = True)

