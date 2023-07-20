#!/usr/bin/python3
"""
a script that starts a Flask web application:
listens on 0.0.0.0, port 5000
Routes:	/: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C” followed by the value of text
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """function for web app home route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """displays /hbnb web app route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """displays value of /c/<text> web app route"""
    text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
