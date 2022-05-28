
from datetime import date, datetime
from asyncpg import Record

from app.db.db import DB
from app.models import Rook

async def getrook() -> Record:
    sql = """SELECT id,name
             FROM rookeries"""
    return await DB.con.fetch(sql)


async def createrook(rook: Rook) -> None:
    sql = """INSERT INTO rookeries( name)
             VALUES ($1)"""
    await DB.con.execute(sql,rook.name)

async def create_rezultat(url: str ,date:datetime, id: int) -> None:
    sql = """INSERT INTO results(photo,dat,rookery_id)
             VALUES ($1,$2,$3) """
    await DB.con.execute(sql,url,date.replace(tzinfo=None),id)

async def get_results_sql(id:int) -> Record:
    sql = """SELECT dat, valruses_number, photo 
             FROM results 
             WHERE rookery_id = $1 """
    return await DB.con.fetch(sql,id)

async def get_results_period(id: int,datestart:datetime,dateend:datetime) -> Record:
    sql = """ SELECT dat, valruses_number, photo 
              FROM results 
              WHERE rookery_id = $1 
              AND dat::date >= $2
              AND dat::date <= $3"""
    return await DB.con.fetch(sql,id,datestart,dateend)
