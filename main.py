import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

# from controller.private_api import app_private
from controller.public_api import app_public
# from model.initializer import init_db

load_dotenv()

# init_db()
origins = ["*"]

app = FastAPI()

# app.mount("/api", app_private)
app.mount("/public", app_public)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(GZipMiddleware)

if __name__ == '__main__':
    if(os.environ["ENV"] == 'prod'):
        print(os.environ["PRIVATE_KEY"])
        print(os.environ["CERT"])

        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True,
                    ssl_keyfile="/etc/letsencrypt/privkey.pem",
                    ssl_certfile="/etc/letsencrypt/cert.pem"
                    )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True
                    )