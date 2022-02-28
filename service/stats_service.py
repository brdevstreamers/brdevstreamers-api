from peewee import *
from dotenv import dotenv_values

from model.user_interaction_model import UserInteraction
config = dotenv_values(".env")

db = SqliteDatabase(config["DB"] + "brdevstreamers.db")

def get_stats():
    cursor = db.execute_sql(
        "SELECT distinct s.user_login, " +
"(SELECT count(*) FROM userinteraction WHERE user_login = s.user_login AND type = 'STREAM_CLICK')," +
"(SELECT count(*) FROM userinteraction WHERE user_login = s.user_login AND type = 'VOD_CLICK')," +
"(SELECT count(*) FROM userinteraction WHERE user_login = s.user_login AND type = 'PREVIEW_CLICK')" +
"FROM userinteraction s ORDER BY s.user_login")

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
    streams = UserInteraction.select().where(UserInteraction.type == 'STREAM_CLICK').count()
    vods = UserInteraction.select().where(UserInteraction.type == 'VOD_CLICK').count()
    previews = UserInteraction.select().where(UserInteraction.type == 'PREVIEW').count()
    stats_summary = {"streams": streams, "vods": vods, "previews": previews}
    return stats_summary

def compute_stat(stat: UserInteraction):
    db_stat = UserInteraction.select().where(UserInteraction.user_login == stat.user_login, 
        UserInteraction.type == stat.type,
        UserInteraction.date == stat.date,
        UserInteraction.interaction_fingerprint == stat.interaction_fingerprint).count()
    if db_stat == 0:
        return UserInteraction.create(user_login=stat.user_login, date=stat.date, type=stat.type, interaction_fingerprint=stat.interaction_fingerprint)
    return None