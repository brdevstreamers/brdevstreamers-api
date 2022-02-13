from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.streamer_service import get_streamers

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():  

    return get_streamers()