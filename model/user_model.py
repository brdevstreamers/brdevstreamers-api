import os
from peewee import PostgresqlDatabase, CharField, Model

db = PostgresqlDatabase(
    os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
)


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
