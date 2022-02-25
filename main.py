import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller.private_api import app_private
from controller.public_api import app_public
from core import settings
from model.initializer import init_db, migrate_db
from view_model.streamer_viewmodel import StreamerViewModel

init_db()
migrate_db()

origins = ["*"]

app = FastAPI()

app.mount("/api", app_private)
app.mount("/public", app_public)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    if settings.ENV == "prod":
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            ssl_keyfile=settings.PRIVATE_KEY,
            ssl_certfile=settings.CERT,
        )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True
                    )
