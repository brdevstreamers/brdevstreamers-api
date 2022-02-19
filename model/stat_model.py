from enum import unique
from peewee import *
from dotenv import dotenv_values
config = dotenv_values(".env")

db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

class Stat(Model):
    user_login = CharField(null=False)
    access_date = DateTimeField(null=False)
    type = CharField(null=False)

    class Meta:
        database = db