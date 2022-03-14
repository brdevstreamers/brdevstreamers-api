
import os
from model.user_model import User
from peewee import *

db = PostgresqlDatabase(
    os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
)


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error executing {func.__name__}. Error: {e}")

    return inner_function


@exception_handler
def get_users_by_name(users):
    users = User.select().where(User.user_login << users).execute()
    db.close()
    return users


@exception_handler
def get_users():
    users = User.select().execute()
    db.close()
    return users


@exception_handler
def get_user_by_login(user_login):
    user = User.select().where(User.user_login == user_login).get()
    db.close()
    return user


@exception_handler
def create_user_model(user):
    res = User.create(
        user_login=user.user_login,
        email=user.email,
        bio=user.bio,
        discord=user.discord,
        instagram=user.instagram,
        linkedin=user.linkedin,
        github=user.github,
        twitter=user.twitter,
    )

    return res


@exception_handler
def update_user_model(user):
    res = (
        User.update(
            {
                User.instagram: user.instagram,
                User.linkedin: user.linkedin,
                User.github: user.github,
                User.twitter: user.twitter,
                User.discord: user.discord,
                User.bio: user.bio,
            }
        )
        .where(User.user_login == user.user_login)
        .execute()
    )
    return res


@exception_handler
def delete_user(user_login):
    res = User.delete().where(User.user_login == user_login).execute()
    return res
