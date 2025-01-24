from database.models import User
from general import db


def add_user(email, first_name, last_name, password):
    user = User(email=email, first_name=first_name, last_name=last_name, password=password)
    db.session.add(user)
    db.session.commit()
    return "User added successfully."


def get_user(username):
    return User.query.filter_by(username=username).first()


def get_all_users():
    return User.query.all()
