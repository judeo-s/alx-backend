#!/usr/bin/env python3
"""
Basic Flask Application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """A route function for the index page
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
