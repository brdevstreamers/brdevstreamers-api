import os
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.github_service import get_contributors

from service.stats_service import compute_stat, get_stats, get_stats_summary
from service.twitch_service import TwitchService
from view_model.stats_viewmodel import StatsViewModel
from view_model.stream_viewmodel import StreamViewModel
from view_model.tag_viewmodel import TagViewModel
from view_model.vod_viewmodel import VodViewModel
from twitchAPI.twitch import Twitch


origins = ["*"]

app_public = FastAPI(openapi_prefix="/public")
twitch = Twitch(os.environ["CLIENT_ID"], os.environ["CLIENT_SECRET"])

app_public.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app_public.get("/streams", response_model=List[StreamViewModel])
async def streams():
    twitch_service = TwitchService(twitch)
    return twitch_service.get_streamers()


@app_public.get("/vods", response_model=List[VodViewModel])
async def vods():
    twitch_service = TwitchService(twitch)
    return twitch_service.get_vods()


@app_public.get("/stats", response_model=List[StatsViewModel])
async def stats():
    return get_stats()


@app_public.get("/tags", response_model=List[TagViewModel])
async def tags():
    twitch_service = TwitchService(twitch)
    return twitch_service.get_tags()


@app_public.get("/stats/summary")
async def stats_summary():
    return get_stats_summary()


@app_public.get("/contributors")
async def contributors():
    return get_contributors()