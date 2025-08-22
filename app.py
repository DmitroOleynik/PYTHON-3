from fastapi import FastAPI
from fastapi.responses import JSONResponse
import aiohttp
from starlette import status

app = FastAPI(
    title="To-Do List API",
    description="Простий API для керування списком завдань",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Tasks",
            "description": "Операції з завданнями (створення, читання, оновлення, видалення)"
        }
    ]
)


to_do_app = {

}


@app.post(
    "/add",
    summary="Додати нове завдання",
    description="Створює нове завдання з вказаним ID та назвою",
    tags=["Tasks"],
    status_code=status.HTTP_201_CREATED
)
async def add_task(_id: int, name: str):
    """
        Додає нове завдання до списку.

        - **_id**: Унікальний ідентифікатор завдання (ціле число)
        - **name**: Назва завдання (рядок)

        Повертає повідомлення про успішне виконання.
        """
    to_do_app[_id] = name
    return "success"


@app.get(
    "/get_all",
    summary="Отримати всі завдання",
    description="Повертає повний список всіх завдань",
    tags=["Tasks"]
)
async def get_all():
    """
        Отримує всі існуючі завдання.

        Повертає словник, де ключ - ID завдання, значення - назва завдання.
        """
    return to_do_app


@app.get(
    "/get_one/{_id}",
    summary="Отримати одне завдання",
    description="Повертає конкретне завдання за його ID",
    tags=["Tasks"]
)
async def get_one(_id: int):
    """
        Отримує конкретне завдання за його ID.

        - **_id**: ID завдання для пошуку

        Якщо завдання не знайдено, повертає HTTP 404 помилку.
        """
    return to_do_app.get(_id)


@app.put(
    "/update/{_id}",
    summary="Оновити завдання",
    description="Оновлює назву існуючого завдання",
    tags=["Tasks"]
)
async def update_task(_id: int, new_name: str):
    """
        Оновлює назву завдання з вказаним ID.

        - **_id**: ID завдання для оновлення
        - **new_name**: Нова назва завдання

        Якщо завдання не знайдено, повертає HTTP 404 помилку.
        Повертає оновлений список всіх завдань.
        """
    to_do_app.update({_id: new_name})
    return to_do_app


@app.delete(
    "/delete/{_id}",
    summary="Видалити завдання",
    description="Видаляє завдання за його ID",
    tags=["Tasks"]
)
async def del_task(_id: int):
    """
        Видаляє завдання з вказаним ID.

        - **_id**: ID завдання для видалення

        Якщо завдання не знайдено, повертає HTTP 404 помилку.
        Повертає повідомлення про успішне видалення.
        """
    del to_do_app[_id]
    return "success"
