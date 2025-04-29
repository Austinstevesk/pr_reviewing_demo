from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = {"foo": {"name": "Foo", "description": "A test item"}}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/{item_id}", status_code=status.HTTP_201_CREATED)
async def create_item(item_id: str, item: dict):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item