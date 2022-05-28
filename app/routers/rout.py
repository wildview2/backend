
from datetime import date, datetime
from fastapi import (APIRouter, BackgroundTasks, File, Form, Query, UploadFile,
                     status)
from pydantic import Field
import pathlib
from fastapi.responses import FileResponse
from app.neiro import background_neiro, create_my_photo
from app.queries.rookeries import create_rezultat, createrook, get_results_period, get_results_sql, getrook
from app.utils.utils import format_records
from app.models import ResultsOut, Rook, RookOut, SuccessfulResponse
from app.routers.download import downloadfilesproduct

_router = APIRouter(tags=["Rook"])



@_router.get("/rookeries",response_model=list[RookOut])
async def get_rook():
    rook = format_records(await getrook(),RookOut)
    return rook

@_router.post("/rookiers/add",response_model=SuccessfulResponse, status_code=status.HTTP_201_CREATED)
async def add_rook(rook: Rook):
        await createrook(rook)
        return SuccessfulResponse()

@_router.post("/rookeries/id/add",response_model=SuccessfulResponse, status_code=status.HTTP_201_CREATED)
async def add_results( data: datetime = Form(..., describe="Время запроса"),
                       id: int = Form(...,describe = "Id лежбища"),
                       upload_file: UploadFile = File(...),
                       background_tasks: BackgroundTasks = Form(...)):
        # добавить творой поток
        background_tasks.add_task(background_neiro, upload_file, id , data)
       # url = await downloadfilesproduct(upload_file)
       # val = await create_my_photo(url)
       # await create_rezultat(url, data, id,val)
        return SuccessfulResponse()

#поправить
@_router.get("/rookeries/{id}/",response_model=list[ResultsOut])
async def get_results(id: int = Query(..., describe = "id лежбища") ):
       rez = format_records(await get_results_sql(id), ResultsOut)
       return rez

@_router.get("/rookeries/{iamge_name}/photo")
async def get_photo_by_name(image_name: str = Query(..., describe = "id лежбища") ):
    folder_path = pathlib.Path(__file__).parent.resolve()
    # проверка на существование файла
    file_path = folder_path.joinpath(pathlib.Path(f"assets/{image_name}"))
    # TODO: Добавить в Exception
    return FileResponse(file_path)

@_router.get("/rookeries/{id}/periods",response_model=list[ResultsOut])
async def get_results_per(id: int = Query(..., describe = "id лежбища"), 
                      datestart: date = Query(..., description="Начальная формата ГГ-ММ-ДД"),
                      dateend: date = Query(..., description="Дата формата ГГ-ММ-ДД")):
       rez = format_records(await get_results_period(id,datestart,dateend), ResultsOut)
       return rez
        



