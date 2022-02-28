from fastapi import FastAPI
from service.stats_service import get_stats, get_stats_summary, compute_stat
from service.streamer_service import get_streamers, get_vods
from fastapi.middleware.cors import CORSMiddleware

from view_model.user_interaction_viewmodel import StatViewModel

origins = ["*"]

app_public = FastAPI(openapi_prefix="/public")

app_public.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app_public.get("/streams")
async def root():
    return get_streamers()


@app_public.get("/vods")
async def vods():
    return get_vods()


@app_public.get("/stats")
async def stats():
    return get_stats()
    

@app_public.get("/stats/summary")
async def stats_summary():
    return get_stats_summary()