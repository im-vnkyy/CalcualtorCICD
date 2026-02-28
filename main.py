from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Calculator API is running!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}