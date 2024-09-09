#!/usr/bin/env python3
"""
Basic Flask Application
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """A class to configure flask applications
    """
    LANGUAGES = ["en", "fr"]

    @staticmethod
    def set_config(app):
        if app:
            app.config["BABEL_DEFAULT_LOCALE"] = Config.LANGUAGES[0]
            app.config["BABEL_DEFAULT_TIMEZONE"] = "UTC"


app = Flask(__name__)
babel = Babel(app)
Config.set_config(app)


@app.route("/")
def index():
    """A route function for the index page
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
