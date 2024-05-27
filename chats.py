from sqlalchemy.sql import text
from db import db

def create_chat(user_id, chat):
    try:
        db.session.execute(text("INSERT INTO Chats (user_id, chat) VALUES (:user_id, :chat)"),
                     {"user_id": user_id, "chat": chat})
        db.session.commit()
        return True
    except Exception as e:
        return False

def get_all():
    try:
        result = db.session.execute(text("SELECT * FROM chats ORDER BY created_at DESC")).fetchall()
        return result if result else []
    except Exception as e:
        return []

def create_comment(user_id, chat_id, comment):
    try:
        db.session.execute(text("INSERT INTO Comments (user_id, chat_id, comment) VALUES (:user_id, :chat_id, :comment)"),
                     {"user_id": user_id, "chat_id": chat_id, "comment": comment})
        db.session.commit()
        return True
    except Exception as e:
        return False

def get_comments():
    try:
        result = db.session.execute(text("SELECT * FROM Comments ORDER BY created_at DESC")).fetchall()
        return result if result else []
    except Exception as e:
        return []