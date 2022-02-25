from enum import unique

from core import settings
from peewee import *

db = SqliteDatabase(settings.DB + "brdevstreamers.db")


class Streamer(Model):
    user_id = CharField(unique=True)
    user_login = CharField(unique=True)
    discord = CharField(unique=False, null=True)
    instagram = CharField(unique=False, null=True)
    linkedin = CharField(unique=False, null=True)
    github = CharField(unique=False, null=True)
    twitter = CharField(unique=False, null=True)

    class Meta:
        database = db