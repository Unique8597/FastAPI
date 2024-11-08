from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

# to run app on reload: uvicorn intro:app --reload
