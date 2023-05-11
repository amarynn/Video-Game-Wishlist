from flask import request, render_template, redirect, session
from models.games_models import all_games, wishlist_items, search_games, add_to_wishlist
from services.session_info import current_user

def index():
    games = all_games()
    return render_template("games/index.html", games = games, current_user = current_user())

def new():
    return render_template("games/new.html")

def no_user():
    return redirect("")

def wishlist_add(id):
    add_to_wishlist(id, session['user_id'])
    return redirect("")

def my_wishlist():
    wishlist = wishlist_items(session['user_id'])
    return render_template("games/wishlist.html", wishlist = wishlist, current_user = current_user())

def search():
    search_term = request.args.get("search_term")
    games = search_games(search_term)
    return render_template("games/index.html", games = games, current_user = current_user())