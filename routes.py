from flask import render_template, request, session, redirect, flash, get_flashed_messages
import datetime
from app import app
import users
import chats

@app.route("/")
def index():
    user = session.get("user_id")
    all_chats = chats.get_all()
    comments = chats.get_comments()
    notifications = get_flashed_messages()
    return render_template("index.html", user=user, chats=all_chats, comments=comments, notifications=notifications)

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

        ''' Fix 4:
        app.logger.warning("Login failed, username: {}, time: {}".format(username, datetime.datetime.now())) '''

        flash("Wrong username or password!")
        return redirect("/")
    return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/create_chat", methods=["POST"])
def create_chat():
    if not session.get("user_id"):
        return redirect("/")
    users.check_csrf()
    user = session["user_id"]
    chat = request.form["chat"]
    result = chats.create_chat(user, chat)
    if result:
        return redirect("/")

    ''' Fix 4:
    app.logger.warning("Chat could not be created, user id: {}, chat: {}, time: {}".format(user, chat, datetime.datetime.now())) '''

    flash("Error in creating new chat!")
    return redirect("/")

@app.route("/new_comment", methods=["POST"])
def new_comment():
    if not session.get("user_id"):
        return redirect("/")

    ''' Flaw 1: Not checking the csrf token '''
    ''' Fix 1:
    users.check_csrf() '''

    user_id = session["user_id"]
    chat_id = request.form["chat_id"]
    comment = request.form["comment"]
    result = chats.create_comment(user_id, chat_id, comment)
    if result:
        return redirect("/")

    ''' Fix 4:
    app.logger.warning("Comment could not be created, user id: {}, chat id: {}, comment: {}, time: {}".format(user_id, chat_id, comment, datetime.datetime.now())) '''

    flash("Error in adding comment!")
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    chat_id = request.form["chat_id"]

    ''' Flaw 5: Not checking user before deleting'''
    ''' Fix 5:
    user_id = session.get("user_id")
    if not user_id:
        flash("Log in to access this website!")
        return redirect("/")

    chat_creator = chats.get_chat_creator(chat_id)
    if chat_creator[0] != user_id:
        flash("You can only delete your own chats!")
        return redirect("/") '''

    chats.delete_chat(chat_id)
    flash("Chat deleted!")
    return redirect("/")

