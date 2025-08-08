from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model for Todo
class Todo(BaseModel):
    id: int
    title: str
    description: str
    done: bool = False

# In-memory DB
todos: List[Todo] = [
    Todo(id=1, title="Learn FastAPI", description="Build a REST API", done=False),
    Todo(id=2, title="Read Book", description="Read ML concepts", done=True)
]

# GET all todos
@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

# GET single todo
@app.get("/todos/{todo_id}", response_model=Todo)
def get_single(todo_id: int):
    todo = next((t for t in todos if t.id == todo_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# POST create todo
@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# PUT update todo
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

# DELETE todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": "Todo deleted"}

from fastapi.responses import FileResponse
import os

@app.get("/favicon.ico")
def favicon():
    return FileResponse(os.path.join("static", "favicon.ico"))
