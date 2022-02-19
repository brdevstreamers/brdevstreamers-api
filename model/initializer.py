from peewee import *
from model.streamer_model import Streamer
from model.stat_model import Stat
from dotenv import dotenv_values

config = dotenv_values(".env")

def init_db():
    db = SqliteDatabase(config["DB"] + "brdevstreamers.db")
    db.connect()
    db.create_tables([Streamer, Stat])
    db.close()