import os
from peewee import PostgresqlDatabase, CharField, IntegerField, Model

db = PostgresqlDatabase(
    os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
)


class Reward(Model):
    id = CharField(null=False)
    description = CharField(null=False)
    price = IntegerField(null=False)
    quantity_available = IntegerField(null=False)

    class Meta:
        database = db
