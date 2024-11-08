from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def list_items():
    return {'message':"items listed"}

@app.get("/items/{item_id}")
async def get_id(item_id:int):
    return {"item id":item_id}

@app.get("/users/me")
async def get_current_user():
    return {"Message":"this is the current user"}
# order matters when putting routes
@app.get("/users/{user_id}")
async def get_id(user_id:str):
    return {"user id":user_id}

