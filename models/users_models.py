from db.db import sql
import bcrypt

def create_user(user_name, email, password):
    password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql("INSERT INTO users(user_name, email, password_digest) VALUES(%s, %s, %s) RETURNING*", [user_name, email, password_digest])

def find_user_by_user_name(user_name):
    users = sql("SELECT * FROM users WHERE user_name = %s", [user_name])
    if len(users) > 0:
        return users[0]
    else:
        return None
    
def find_user_by_id(id):
    users = sql("SELECT * FROM users WHERE id = %s", [id])
    return users[0]

def update_user(id, user_name, email, password):
    password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql("UPDATE users SET user_name = %s, email = %s, password_digest = %s WHERE id = %s RETURNING*", [user_name, email, password_digest, id])