from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from service.streamer_service import get_streamers, get_vods

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "https://brstreamers.dev",
    "https://brstreamers.dev:8000",
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

@app.get("/vods")
async def vods():  
    return get_vods()


    
if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                # ssl_keyfile="/etc/letsencrypt/live/brstreamers.dev/privkey.pem", 
                # ssl_certfile="/etc/letsencrypt/live/brstreamers.dev/cert.pem"
                )