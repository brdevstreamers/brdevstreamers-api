from enum import unique
from peewee import *
from dotenv import dotenv_values
config = dotenv_values(".env")

db = PostgresqlDatabase(config['DB_NAME'], user=config['DB_USER'],
                           password=config['DB_PASS'], host=config['DB_HOST'], port=config['DB_PORT'])

class User(Model):
    user_login = CharField(unique=True)
    discord = CharField(unique=False, null=True)
    instagram = CharField(unique=False, null=True)
    linkedin = CharField(unique=False, null=True)
    github = CharField(unique=False, null=True)
    twitter = CharField(unique=False, null=True)
    email = CharField(unique=True, null=False)
    bio = CharField(unique=False, null=True)

    class Meta:
        database = db