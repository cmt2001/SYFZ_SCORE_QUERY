from app import flask_app

if __name__ == "__main__":
    flask_app.debug = flask_app.config['DEBUG']
    flask_app.run(port=8089)