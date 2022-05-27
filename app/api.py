
from fastapi import FastAPI

from app.db.db import DB


app = FastAPI(title='Marketplace')


@app.on_event('startup')
async def startup() -> None:
    await DB.connect_db()

@app.on_event('shutdown')
async def shutdown() -> None:
    await DB.connect_db()



