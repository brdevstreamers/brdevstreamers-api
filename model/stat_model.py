from core import settings
from peewee import *

db = SqliteDatabase(settings.DB + "brdevstreamers.db")


class Stat(Model):
    user_login = CharField(null=False)
    access_date = DateField(null=False)
    type = CharField(null=False)
    fingerprint = CharField(null=False)

    class Meta:
        database = db