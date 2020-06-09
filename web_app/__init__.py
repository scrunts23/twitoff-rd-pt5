# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask
from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.tweet_routes import tweet_routes
from web_app.routes.twitter_routes import twitter_routes

DATABASE_URI = "sqlite:///twitoff_development.db" # using relative filepath


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    app.register_blueprint(twitter_routes)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)