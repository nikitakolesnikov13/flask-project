from flask import abort, jsonify, redirect, render_template, request, url_for
from flask_migrate import Migrate
import sys

from init import create_app
from models import db, Cats

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    return redirect(url_for("get_todos_from_list", list_id=1))


# JSON
@app.route("/cats", methods=["POST"])
def cats_list_view():
    responseBody = {}
    error = False
    try:
        name = request.get_json()["name"]
        list = Cats(name=name)
        responseBody["msg"] = "cat has been created"
        db.session.add(list)
        db.session.commit()
        responseBody["id"] = list.id
        responseBody['name'] = list.name
    except Exception as e:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error:
            abort(400)
        else:
            return jsonify(responseBody)


# web
