import os
from flask import Flask
from routes.games_routes import games_routes
# from routes.sessions_routes import sessions_routes
# from routes.users_routes import users_routes

SECRET_KEY = os.environ.get("SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(games_routes, url_prefix = "/games")
# app.register_blueprint(users_routes, url_prefix = "/users")
# app.register_blueprint(sessions_routes, url_prefix = "/sessions")