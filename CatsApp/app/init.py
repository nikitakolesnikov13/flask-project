from flask import Flask, jsonify, request

from routes import init_routes


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev_key"
    # alternative configuration based on if is test env or not
    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost:5433/"
    elif test_config == "test":
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost-test:5433/"

    @app.errorhandler(404)
    def not_found(error):
        app.logger.info(
            f"404 => user tried to access route {request.full_path}"
        )
        return jsonify({
            "msg": "resource not found, aborting...",
            "success": False,
            "data": None
        }), 404

    # initialisation des routes
    init_routes(app)

    return app
