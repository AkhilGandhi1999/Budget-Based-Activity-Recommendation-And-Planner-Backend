import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import recommandations
    app.register_blueprint(recommandations.bp)

    from . import categories
    app.register_blueprint(categories.bp)

    return app