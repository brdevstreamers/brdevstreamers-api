from enum import unique
from peewee import *
from dotenv import dotenv_values
config = dotenv_values(".env")

db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

class UserInteraction(Model):
    user_id= CharField(null=False)
    date = DateField(null=False)
    interaction_fingerprint = CharField(null=False)

    class Meta:
        database = db