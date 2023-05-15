from flask import request, render_template, redirect, session
from models.games_models import all_games, wishlist_items, search_games, add_to_wishlist, add_game, delete_game, specific_game, update_game, delete_from_wishlist, all_wishlist_items
from services.session_info import current_user

def index():
    games = all_games()
    if session.get("user_id"):
        wishlist = all_wishlist_items(session['user_id'])
        return render_template("games/index.html", games = games, wishlist = wishlist, current_user = current_user())
    else: 
        return render_template("games/index.html", games = games, wishlist = [], current_user = current_user())

def new():
    return render_template("games/new.html", current_user = current_user())

def new_game():
    name = request.form.get("name")
    image_url = request.form.get("image_url")
    description = request.form.get("description")
    add_game(name, image_url, description)
    return redirect("/")

def wishlist_add(id):
    add_to_wishlist(id, session['user_id'])
    return redirect("/")

def my_wishlist():
    wishlist = wishlist_items(session['user_id'])
    return render_template("games/wishlist.html", wishlist = wishlist, current_user = current_user())

def remove_from_wishlist(id):
    delete_from_wishlist(session['user_id'], id)
    return redirect("/games/my_wishlist")

def search():
    search_term = request.args.get("search_term")
    games = search_games(search_term)
    return render_template("games/index.html", games = games, current_user = current_user())

def edit():
    games = all_games()
    return render_template("games/edit.html", games = games, current_user = current_user())

def edit_game(id):
    game = specific_game(id)
    return render_template("games/edit_game.html", game = game, current_user = current_user())

def change_game_details(id):
    name = request.form.get("name")
    image_url = request.form.get("image_url")
    description = request.form.get("description")
    update_game(id, name, image_url, description)
    return redirect("/games/edit")

def delete(id):
    delete_game(id)
    return redirect("/games/edit")