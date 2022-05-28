
from datetime import datetime
from fastapi import Form
from pydantic import BaseModel, Field


class Rook(BaseModel):
    name : str = Field(..., title='Имя лежбища')
    # может добавить долготу и высоту для лежбища


class SuccessfulResponse(BaseModel):
    details: str = Field('Выполнено', title='Статус операции')


class RookOut(BaseModel):
    id: int = Field(None, title='ID лежбища', gt=0)
    name: str = Field(..., title='Имя лежбища')
    # может добавить долготу и высоту для лежбища

class ResultsOut(BaseModel):
    dat: datetime = Field(None, title='Время фотки')
    valruses_number: int =Field(..., title='ID лежбища')
    photo: str = Field(..., title='ID лежбища')