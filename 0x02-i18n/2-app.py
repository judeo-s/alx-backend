#!/usr/bin/env python3
"""
Basic Flask Application
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config for the app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def index():
    """A route function for the index page
    """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """Get the locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
