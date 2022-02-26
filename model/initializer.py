from peewee import *
from dotenv import dotenv_values
from playhouse.migrate import *
from model.reward_model import Reward
from model.user_interaction_model import UserInteraction

from model.user_model import User 

config = dotenv_values(".env")
db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

def init_db():   
    db.connect()
    db.create_tables([User, UserInteraction, Reward])
    db.close()
