CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    user_name TEXT,
    email TEXT,
    password_digest TEXT
);

CREATE TABLE games(
    id SERIAL PRIMARY KEY,
    name TEXT,
    image_url TEXT,
    description TEXT
);

CREATE TABLE user_wishlist(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    game_id INTEGER 
);