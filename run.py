# -*- coding: utf-8 -*-
from main import flask_app

if __name__ == "__main__":
    flask_app.debug = flask_app.config['DEBUG']
    flask_app.run(host='0.0.0.0',port=80)