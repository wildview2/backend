
import datetime
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

class MessageOut(BaseModel):
    tg_id: int = Field(None, title='Telegram ID', gt=0)
    chat_id: int = Field(None, title='ID чата')
    body: str = Field(..., title='Тело сообщения')
    date: datetime = Field(..., title='Время отправки сообщения')