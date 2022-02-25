from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.stats_service import compute_stat, get_stats, get_stats_summary
from service.streamer_service import get_streamers, get_vods
from view_model.stat_viewmodel import StatViewModel

origins = ["*"]

app_public = FastAPI(openapi_prefix="/public")

app_public.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app_public.get("/")
async def root():
    return get_streamers()


@app_public.get("/vods")
async def vods():
    return get_vods()



@app_public.post("/stats")
async def stats(stat: StatViewModel):
    return compute_stat(stat)



@app_public.get("/stats")
async def stats():
    return get_stats()
    

@app_public.get("/stats/summary")
async def stats_summary():
    return get_stats_summary()