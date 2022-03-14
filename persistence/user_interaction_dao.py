import os
from peewee import *
from model.user_interaction_model import UserInteraction
from model.user_model import User


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
def get_user_interactions_by_user_login(user_login):
    user_interactions = (
        UserInteraction.select().where(UserInteraction.user_login == user_login).execute()
    )
    db.close()
    return user_interactions
