from fastapi import FastAPI
from fastapi.responses import JSONResponse
import aiohttp


app = FastAPI()


to_do_app = {

}


@app.post("/add")
async def add_task(_id: int, name: str):
    to_do_app[_id] = name
    return "success"


@app.get("/get_all")
async def get_all():
    return to_do_app


@app.get("/get_one")
async def get_one(_id: int):
    return to_do_app.get(_id)


@app.put("/update")
async def update_task(_id: int, new_name: str):
    to_do_app.update({_id: new_name})
    return to_do_app


@app.delete("/del")
async def del_task(_id: int):
    del to_do_app[_id]
    return "success"
