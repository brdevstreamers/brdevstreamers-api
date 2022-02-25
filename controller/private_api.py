from http.client import HTTPException
from urllib.request import Request

from core import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.streamer_model import Streamer
from starlette.responses import JSONResponse
from view_model.streamer_viewmodel import StreamerViewModel

origins = ["*"]


app_private = FastAPI(openapi_prefix="/api")

app_private.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app_private.middleware("http")
async def verify_user_agent(request: Request, call_next):
    try:
        if request.headers["token"] == settings.API_TOKEN:
            response = await call_next(request)
            return response
    except Exception as e:
        print(e)
        return JSONResponse(content={
        "message": "Unauthorized"
    }, status_code=401)
    

@app_private.get("/streamers")
async def streamer():
    try:
        streamers = Streamer.select().get()
        return streamers
    except:
        raise HTTPException(status_code=404, detail="Streamers not found")


@app_private.get("/streamer/{user_login}")
async def streamer(user_login: str):
    try:
        return Streamer.select().where(Streamer.user_login == user_login).get()
    except:
        raise HTTPException(status_code=404, detail="Streamer not found")


@app_private.post("/streamer")
async def save_streamer(streamer: StreamerViewModel):
    return Streamer.create(user_id=streamer.user_id, 
        user_login=streamer.user_login,
        discord = streamer.discord,
        instagram = streamer.instagram,
        linkedin = streamer.linkedin,
        github = streamer.github,
        twitter = streamer.twitter)
        

@app_private.put("/streamer")
async def update_streamer(streamer: StreamerViewModel):
    res = (Streamer
       .update({Streamer.instagram: streamer.instagram,
                Streamer.linkedin: streamer.linkedin,
                Streamer.github: streamer.github,
                Streamer.twitter: streamer.twitter,
                Streamer.discord: streamer.discord})
       .where(Streamer.user_login == streamer.user_login)
       .execute())
    return res
        

@app_private.delete("/streamer/{user_login}")
async def delete_streamer(user_login):
    try:
        streamer = Streamer.delete().where(Streamer.user_login == user_login).execute()
        return "OK"
    except:
        raise HTTPException(status_code=404, detail="Streamer not found")
