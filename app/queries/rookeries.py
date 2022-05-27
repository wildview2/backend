
from datetime import datetime
from asyncpg import Record

from app.db.db import DB
from app.models import Rook

async def getrook() -> Record:
    sql = """SELECT id,name
             FROM rookiers"""
    return await DB.fetch(sql)

async def createrook(rook: Rook) ->None:
    sql = """INSERT INTO rookiers( name)
             VALUES ($2)"""
    await DB.execute(sql,rook.name)


async def create_rezultat(url:str ,datetime: datetime):
    sql = """INSERT INTO rookiers()
             VALUES ($2) """