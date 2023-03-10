from flask import jsonify


# routes factory
def init_routes(app):

    @app.route("/api", methods=["GET"])
    def get_api_base_url():
        return jsonify({
            "msg": "Cats api is up",
            "success": True,
            "data": None
        }), 200