from flask import request, render_template, redirect
from models.users_models import create_user, find_user_by_id, update_user

def new():
    return render_template("users/new.html")

def edit(id):
    user_details = find_user_by_id(id)
    return render_template("users/edit.html", user_details = user_details)

def create():
    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    create_user(user_name, email, password)
    return redirect("/")

def update(id):
    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    update_user(id, user_name, email, password)
    return redirect("/")