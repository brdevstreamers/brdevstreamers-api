import os
from model.reward_model import Reward
from model.user_interaction_model import UserInteraction
from model.user_model import User
from peewee import PostgresqlDatabase

# db = PostgresqlDatabase(
#     config["DB_NAME"],
#     user=config["DB_USER"],
#     password=config["DB_PASS"],
#     host=config["DB_HOST"],
#     port=config["DB_PORT"],
# )


# def init_db():
    # db.connect(reuse_if_open=True)
    # db.create_tables([User, UserInteraction, Reward])
    # db.close()
