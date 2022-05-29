
from fastapi import FastAPI, Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.db.db import DB
from fastapi.responses import JSONResponse
from app.exceptions import CommonException, InternalServerError
from fastapi.exceptions import RequestValidationError
from app.routers.rout import _router
import logging
import time
from logging import getLogger
from starlette.middleware.cors import CORSMiddleware

logger = getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
origins = ["*"]

app = FastAPI(title='BackHack')


@app.middleware("http")
async def log_requst(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = (time.perf_counter() - start_time)
    formatted_process_time = '{0:.5f}'.format(process_time)
    logger.info(f"""***INFO*** Date time: {time.ctime()}  path={request.url.path} Method {request.method}
                Completed_in = {formatted_process_time}s""")
    return response


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"***ERROR*** Status code 422 Message: {str(exc)}")
    return JSONResponse(
        status_code=422,
        content={'details': exc.errors()}
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception(request, exc):
    logger.error(f"***ERROR*** Status code {exc.status_code} Message: {exc.detail}")
    return JSONResponse(
        content={"detail": exc.detail},
        status_code=exc.status_code,
    )


@app.exception_handler(Exception)
async def common_exception_handler(request: Request, exception: Exception):
    error = InternalServerError(debug=str(exception))
    logger.error(f"***ERROR*** Status code {error.status_code} Message: {error.message}")
    return JSONResponse(
        status_code=error.status_code,
        content=error.to_json()
    )

@app.exception_handler(CommonException)
async def unicorn_api_exception_handler(request: Request, exc: CommonException):
    logger.error(f"***ERROR*** Status code {exc.code} Message: {exc.error}")
    return JSONResponse(
        status_code=exc.code,
        content=exc.error
    )   


@app.on_event('startup')
async def startup() -> None:
    await DB.connect_db()

@app.on_event('shutdown')
async def shutdown() -> None:
    await DB.connect_db()

app.include_router(_router)
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)



