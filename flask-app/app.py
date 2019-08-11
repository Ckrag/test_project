#!/usr/bin/python3

import json

from flask import Flask
from flask import abort
from flask import make_response
from flask import render_template
from flask import request
from flask_basicauth import BasicAuth

from model.dms import DMS as DMS_APPLICATION

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def say_hello() -> str:
    return "hello to you!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
