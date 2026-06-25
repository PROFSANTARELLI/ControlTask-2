from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

from backend import database, models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# IMPORTANTE: criar tabelas no startup (CI-safe)
@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)


# =========================
# SCHEMAS
# =========================

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None


class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    priority: str
    status: str

    class Config:
        from_attributes = True


# =========================
# USERS
# =========================

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    exists = db.query(models.User).filter(models.User.email == user.email).first()
    if exists:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    db_user = models.User(
        name=user.name,
        email=user.email,
        password_hash=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# =========================
# TASKS
# =========================

@app.post("/users/{user_id}/tasks", response_model=TaskResponse, status_code=201)
def create_task(user_id: int, task: TaskCreate, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db_task = models.Task(
        user_id=user_id,
        title=task.title,
        description=task.description,
       if task.priority.upper() not in ["LOW", "MEDIUM", "HIGH"]:
    raise ValueError("Prioridade inválida")

priority=task.priority.upper()
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/users/{user_id}/tasks", response_model=List[TaskResponse])
def list_tasks(user_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    payload = data.model_dump(exclude_unset=True)

    for k, v in payload.items():
        if k in ["priority", "status"]:
            setattr(task, k, v.upper())
        else:
            setattr(task, k, v)

    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db.delete(task)
    db.commit()
    return None
