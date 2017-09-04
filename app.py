#!/usr/bin/python

from flask import Flask
import os

app = Flask(__name__)

# VMS


@app.route("/")
def hello():
    """
    say hello
    """  
    vms = [1, 2, 3]
    # return render_template('index.html', title='Home', vms)
    return "Hello, World version 3!\n"


def run():
    app.run(host='0.0.0.0', port=9000)


if __name__ == '__main__':
    run()
