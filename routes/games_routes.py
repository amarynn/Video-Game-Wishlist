from flask import Blueprint
from controllers.games_controller import index, new, no_user, my_wishlist, search, wishlist_add

games_routes = Blueprint("games_routes", __name__)

games_routes.route("")(index)
games_routes.route("/new")(new)
games_routes.route("/no_user")(no_user)
games_routes.route("/<id>/wishlist", methods = ['POST'])(wishlist_add)
games_routes.route("/my_wishlist")(my_wishlist)
games_routes.route("/search")(search)