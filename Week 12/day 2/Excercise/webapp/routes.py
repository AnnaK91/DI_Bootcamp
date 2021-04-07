# Create an add_city page (have in mind you must have a view, route and a template) where a user can add a city to your website. The template must have a Form in order for the user to post the new city details.
# The form should contain the following fields:
# city’s name
# city’s country
# number of inhabitants
# city’s area (in square km)

import flask
from flask import Flask, render_template, redirect, url_for
from . import app # . is webapp/

from . import forms


@app.route("/")

def homepage():
    return "Welcome to my website"


@app.route("/add-cities", methods=["GET","POST"])

def addcity():

    form = forms.AddCities()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            citys_name = form.citys_name.data
            citys_country = form.citys_country.data
            number_of_inhabitants = form.number_of_inhabitants.data
            citys_area = form.citys_area.data

    return flask.render_template("city_form.html", form=form)