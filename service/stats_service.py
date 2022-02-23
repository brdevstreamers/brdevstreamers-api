from model.stat_model import Stat
from peewee import *
from dotenv import dotenv_values
config = dotenv_values(".env")

db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

def get_stats():
    cursor = db.execute_sql(
        "SELECT distinct s.user_login, " +
"(SELECT count(*) FROM stat WHERE user_login = s.user_login AND type = 'STREAM')," +
"(SELECT count(*) FROM stat WHERE user_login = s.user_login AND type = 'VOD')," +
"(SELECT count(*) FROM stat WHERE user_login = s.user_login AND type = 'PREVIEW')" +
"FROM stat s ORDER BY s.user_login")

    stats = []

    for row in cursor.fetchall():
        stat = {}
        stat['user_login'] = row[0]
        stat['stream_clicks'] = row[1]
        stat['vod_clicks'] = row[2]
        stat['preview_clicks'] = row[3]
        stats.append(stat)

    return stats
       
def get_stats_summary():
    streams = Stat.select().where(Stat.type == 'STREAM').count()
    vods = Stat.select().where(Stat.type == 'VOD').count()
    previews = Stat.select().where(Stat.type == 'PREVIEW').count()
    stats_summary = {"streams": streams, "vods": vods, "previews": previews}
    return stats_summary

def compute_stat(stat: Stat):
    db_stat = Stat.select().where(Stat.user_login == stat.user_login, 
        Stat.type == stat.type,
        Stat.access_date == stat.access_date,
        Stat.fingerprint == stat.fingerprint).count()
    if db_stat == 0:
        return Stat.create(user_login=stat.user_login, access_date=stat.access_date, type=stat.type, fingerprint=stat.fingerprint)
    return None