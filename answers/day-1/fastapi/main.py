from fastapi import FastAPI, Request
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    message: str

@app.get("/get")
async def get_method(request: Request):
    params = request.query_params
    return {
        "message": "Success Get Request",
        "params": params
        }

@app.post("/post")
async def post_method(item: Item):
    return {
        "message": "Success Post Request",
        "item": item
    }

@app.delete("/delete")
async def delete_method():
    return {"message": "Success Delete Request"}

@app.put("/put")
async def put_method():
    return {"message": "Success Put Request"}