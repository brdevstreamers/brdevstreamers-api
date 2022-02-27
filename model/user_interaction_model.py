from enum import unique
from peewee import *
from dotenv import dotenv_values
config = dotenv_values(".env")

db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

class UserInteraction(Model):
    user_login= CharField(null=False)
    target_user = CharField(null=True)
    date = DateField(null=False)
    type = CharField(null=False)
    interaction_fingerprint = CharField(null=False)

    class Meta:
        database = db