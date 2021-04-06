from products_data import retrieve_all_products, retrieve_requested_product

import flask
from flask import Flask, render_template, redirect, url_for


# Create a controller using flask.Flask class
app = flask.Flask(__name__)     # __name__ is the name of the file

all_products = retrieve_all_products()
cart_item = []