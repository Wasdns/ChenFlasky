#!/usr/bin/env python

from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1> Make P4 Great Again! </h1>'

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()