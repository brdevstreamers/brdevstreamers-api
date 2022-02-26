from enum import unique
from peewee import *
from dotenv import dotenv_values
config = dotenv_values(".env")

db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

class Reward(Model):
    id= CharField(null=False)
    description = CharField(null=False)
    price = IntegerField(null=False)
    quantity_available = IntegerField(null=False)

    class Meta:
        database = db