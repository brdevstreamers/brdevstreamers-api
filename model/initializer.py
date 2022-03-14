
import os
from model.reward_model import Reward
from model.user_interaction_model import UserInteraction
from model.user_model import User
from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
)


def init_db():
    db.connect(reuse_if_open=True)
    db.create_tables([User, UserInteraction, Reward])
    db.close()
