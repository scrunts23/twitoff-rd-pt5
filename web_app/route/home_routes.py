# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("HOME PAGE")
    return "Twittoff !"


@home_routes.route("/about")
def about():
    print("ABOUT PAGE")
    return "Twittoff App!"