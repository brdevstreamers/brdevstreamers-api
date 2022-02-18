
from urllib.request import Request
from model.initializer import init_db
from model.streamer_model import Streamer
from service.streamer_service import get_streamers, get_vods
from dotenv import dotenv_values
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from starlette.responses import JSONResponse, Response


from view_model.streamer_viewmodel import StreamerViewModel

config = dotenv_values(".env")

app_public = FastAPI(openapi_prefix="/public")
app_api = FastAPI(openapi_prefix="/api")

init_db()

origins = ["*"]

app_public.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app_api.middleware("http")
async def verify_user_agent(request: Request, call_next):
    try:
        if request.headers['token'] == config['API_TOKEN']:
            response = await call_next(request)
            return response
    except:
        print('Unauthorized')

    return JSONResponse(content={
        "message": "Unauthorized"
    }, status_code=401)


@app_public.get("/")
async def root():
    return get_streamers()


@app_public.get("/vods")
async def vods():
    return get_vods()


@app_api.get("/streamers")
async def streamer():
    try:
        streamers = Streamer.select().get()
        return streamers
    except:
        raise HTTPException(status_code=404, detail="Streamers not found")


@app_api.get("/streamer/{user_login}")
async def streamer(user_login: str):
    try:
        return Streamer.select().where(Streamer.user_login == user_login).get()
    except:
        raise HTTPException(status_code=404, detail="Streamer not found")


@app_api.post("/streamer")
async def save_streamer(streamer: StreamerViewModel):
    return Streamer.create(user_id=streamer.user_id, 
        user_login=streamer.user_login,
        discord = streamer.discord,
        instagram = streamer.instagram,
        linkedin = streamer.linkedin,
        github = streamer.github,
        twitter = streamer.twitter)
        



@app_api.delete("/streamer/{user_login}")
async def delete_streamer(user_login):
    try:
        streamer = Streamer.delete().where(Streamer.user_login == user_login).execute()
        return "OK"
    except:
        raise HTTPException(status_code=404, detail="Streamer not found")

app = FastAPI()

app.mount("/api", app_api)
app.mount("/public", app_public)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    if(config["ENV"] == 'prod'):
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True,
                    ssl_keyfile=config["PRIVATE_KEY"],
                    ssl_certfile=config["CERT"]
                    )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True
                    )
