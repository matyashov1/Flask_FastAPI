from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional

app = FastAPI()


class Task(BaseModel):
    title: str
    description: str
    status: bool


tasks_db: Dict[int, Task] = {}
task_id_counter = 0


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return list(tasks_db.values())


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: Task):
    global task_id_counter
    task_id_counter += 1
    tasks_db[task_id_counter] = task
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = task
    return task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": "Task deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
