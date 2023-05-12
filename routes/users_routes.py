from flask import Blueprint
from controllers.users_controller import new, create, edit, update

users_routes = Blueprint("users_routes", __name__)

users_routes.route("/new")(new)
users_routes.route("/create", methods = ["POST"])(create)
users_routes.route("/<id>/edit")(edit)
users_routes.route("/<id>/update", methods = ["POST"])(update)