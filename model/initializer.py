from peewee import *
from model.streamer_model import Streamer


def init_db():
    db = SqliteDatabase('brdevstreamers.db')
    db.connect()
    db.create_tables([Streamer])
    db.close()