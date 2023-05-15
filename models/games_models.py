from db.db import sql

def all_games():
    return sql('SELECT * FROM games ORDER BY name')

def wishlist_items(user_id):
    return sql("SELECT * FROM user_wishlist INNER JOIN games ON user_wishlist.game_id = games.id WHERE user_id = %s ORDER BY name", [user_id])

def search_games(search_term):
    search_parameter = f"%{search_term}%"
    return sql("SELECT * FROM games WHERE UPPER(name) LIKE UPPER(%s)", [search_parameter])

def add_to_wishlist(game_id, user_id):
    sql("INSERT INTO user_wishlist(user_id, game_id) VALUES(%s, %s) RETURNING*", [user_id, game_id])

def delete_from_wishlist(user_id, game_id):
    sql("DELETE FROM user_wishlist WHERE user_id = %s AND game_id = %s RETURNING*", [user_id, game_id])

def add_game(name, image_url, description):
    sql("INSERT INTO games(name, image_url, description) VALUES(%s, %s, %s) RETURNING*", [name, image_url, description])

def delete_game(id):
    sql("DELETE FROM games WHERE id = %s RETURNING*", [id])

def specific_game(id):
    game = sql("SELECT * FROM games WHERE id = %s", [id])
    return game[0]

def update_game(id, name, image_url, description):
    sql("UPDATE games SET name = %s, image_url = %s, description = %s WHERE id = %s RETURNING*", [name, image_url, description, id])

def all_wishlist_items(id):
    random = sql("SELECT game_id FROM user_wishlist WHERE user_id = %s", [id])
    game_ids = []
    for item in random:
        game_ids.append(item['game_id'])
    return game_ids