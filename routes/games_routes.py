from flask import Blueprint
from controllers.games_controller import index, new, my_wishlist, search, wishlist_add, new_game, edit, edit_game, delete, change_game_details, remove_from_wishlist

games_routes = Blueprint("games_routes", __name__)

games_routes.route("/")(index)
games_routes.route("/games/new")(new)
games_routes.route("/games/new_game", methods = ["POST"])(new_game)
games_routes.route("/games/<id>/wishlist", methods = ['POST'])(wishlist_add)
games_routes.route("/games/my_wishlist")(my_wishlist)
games_routes.route("/games/<id>/wishlist_remove", methods = ["POST"])(remove_from_wishlist)
games_routes.route("/games/search")(search)
games_routes.route("/games/edit")(edit)
games_routes.route("/games/<id>/edit")(edit_game)
games_routes.route("/games/<id>/new_game_details", methods = ["POST"])(change_game_details)
games_routes.route("/games/<id>/delete", methods = ["POST"])(delete)