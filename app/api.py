
from fastapi import FastAPI

from app.db.db import DB

from app.routers.rout import _router

app = FastAPI(title='BackHack')


@app.on_event('startup')
async def startup() -> None:
    await DB.connect_db()

@app.on_event('shutdown')
async def shutdown() -> None:
    await DB.connect_db()

app.include_router(_router)

