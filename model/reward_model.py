from enum import unique
from peewee import *
from dotenv import dotenv_values
config = dotenv_values(".env")

db = PostgresqlDatabase(config['DB_NAME'], user=config['DB_USER'],
                           password=config['DB_PASS'], host=config['DB_HOST'], port=config['DB_PORT'])

class Reward(Model):
    id= CharField(null=False)
    description = CharField(null=False)
    price = IntegerField(null=False)
    quantity_available = IntegerField(null=False)

    class Meta:
        database = db