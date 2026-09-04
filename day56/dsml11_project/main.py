from webbrowser import get

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
	return {"message": "Hello World! FastAPI is working fine"}


@get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
	return {"item_id": item_id, "q": q}
