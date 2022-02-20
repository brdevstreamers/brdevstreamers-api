from peewee import *
from model.streamer_model import Streamer
from model.stat_model import Stat
from dotenv import dotenv_values
from playhouse.migrate import * 

config = dotenv_values(".env")
db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

def init_db():   
    db.connect()
    db.create_tables([Streamer, Stat])
    db.close()


def migrate_db():
    migrator = SqliteMigrator(db)
    db.connect()

    try:
        fingerprint_field = CharField(null=True)
        migrate(
            migrator.add_column('stat', 'fingerprint', fingerprint_field),
        ) 
    except:
        pass
    finally:
        db.close()
        print("Migration complete")