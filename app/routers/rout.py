
from datetime import datetime
from pydoc import describe
from fastapi import (APIRouter, File, Form, Query, UploadFile,
                     status)

from app.queries.rookeries import create_results, createrook, getrook
from app.utils.utils import format_records
from app.models import Rook, RookOut, SuccessfulResponse
from app.routers.download import downloadfilesproduct

_router = APIRouter(tags=["Rook"])



@_router.get("/rookeries",response_model=list[RookOut])
async def get_rook():
    rook = format_records(getrook())
    return rook

@_router.post("/rookiers/add",response_model=SuccessfulResponse, status_code=status.HTTP_201_CREATED)
async def add_rook(rook:Rook):
        createrook(Rook)
        return SuccessfulResponse

@_router.post("/rookeries/{id}/add",response_model=SuccessfulResponse, status_code=status.HTTP_201_CREATED)
async def add_results( upload_file: UploadFile = File(...),
                       date: datetime = Form(..., describe="Время запроса"),
                       id: int = Form(..., describe="id лежбища")  ):
        url = await downloadfilesproduct(upload_file)
        create_results(url, date, id)
        return SuccessfulResponse

        
    

#@_router.get("/rookeries/{id}")
#async def get_results():

