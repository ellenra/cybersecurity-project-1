from flask import render_template, request, session, redirect
from app import app
import users
import chats

@app.route("/")
def index():
    user = session.get("user_id")
    all_chats = chats.get_all()
    comments = chats.get_comments()
    return render_template("index.html", user=user, chats=all_chats, comments=comments)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    username = request.form["username"]
    password = request.form["password"]
    result = users.register(username, password)
    if result is True:
        return redirect("/")
    return render_template("register.html", notification=True, message=f"{result}")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if not users.login(username, password):
        return render_template("index.html", notification=True,
                               message="Wrong username or password!")
    return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/create_chat", methods=["POST"])
def create_chat():
    if not session.get("user_id"):
        return redirect("/")
    user = session["user_id"]
    chat = request.form["chat"]
    result = chats.create_chat(user, chat)
    if result:
        return redirect("/")
    return render_template("index.html", user=user, notification=True, message="Error in creating new chat.")

@app.route("/new_comment", methods=["POST"])
def new_comment():
    if not session.get("user_id"):
        return redirect("/")
    user_id = session["user_id"]
    chat_id = request.form["chat_id"]
    comment = request.form["comment"]
    result = chats.create_comment(user_id, chat_id, comment)
    if result:
        return redirect("/")
    return render_template("index.html", user=user_id, notification=True, message="Error in adding comment.")
