import os

from flask import Flask
from . import users

def create_app():
    # create and configure the app
    app = Flask(__name__, static_url_path='/static/')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # from . import blog
    app.register_blueprint(users.bp)
    app.add_url_rule('/', endpoint='index')

    return app