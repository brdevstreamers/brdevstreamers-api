
import os
from peewee import PostgresqlDatabase, CharField, DateField, Model


db = PostgresqlDatabase(
    os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
)


class UserInteraction(Model):
    user_login = CharField(null=False)
    target_user = CharField(null=True)
    date = DateField(null=False)
    type = CharField(null=False)
    interaction_fingerprint = CharField(null=False)

    class Meta:
        database = db
