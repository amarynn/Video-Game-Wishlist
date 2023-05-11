from db.db import sql

def all_games():
    return sql('SELECT * FROM games ORDER BY name')

def wishlist_items(user_id):
    return sql("SELECT * FROM user_wishlist INNER JOIN games ON user_wishlist.game_id = games.id WHERE user_id = %s", [user_id])

def search_games(search_term):
    search_parameter = f"%{search_term}%"
    return sql("SELECT * FROM games WHERE name LIKE (%s)", [search_parameter])

def add_to_wishlist(game_id, user_id):
    sql("INSERT INTO user_wishlist(user_id, game_id) VALUES(%s, %s) RETURNING*", [user_id, game_id])