import math
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from src.configs.database import get_session
from src.apis.tasks.models import Task, BodyCreateDto, BodyUpdateDto

class TaskController:
    def create(payload: BodyCreateDto, db: Session = Depends(get_session)):
        task_to_db = Task.model_validate(payload)
        db.add(task_to_db)
        db.commit()
        db.refresh(task_to_db)
        return task_to_db
    
    def list(limit: int, page: int, db: Session = Depends(get_session)):
        tasks = db.exec(select(Task).offset(page - 1).limit(limit)).all()

        total_tasks = len(db.exec(select(Task)).all())
        total_pages = math.ceil(total_tasks/limit)
       
        return tasks, total_pages
    
    def get_by_id(id:int, db: Session = Depends(get_session)):
        task = db.get(Task, id)
        
        if not task:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Task not found"
            )
        
        return task
    
    def update_by_id(id:int, payload: BodyUpdateDto, db: Session = Depends(get_session)):
        task_to_update = db.get(Task, id)
        if not task_to_update:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Task not found"
            )

        task_data =  payload.model_dump(exclude_unset=True)
        for key, value in task_data.items():
            setattr(task_to_update, key, value)
        
        db.add(task_to_update)
        db.commit()
        db.refresh(task_to_update)

        return task_to_update

    def delete_by_id(id:int, db: Session = Depends(get_session)):
        task = db.get(Task, id)
        
        if not task:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Task not found"
            )
        
        db.delete(task)
        db.commit()

        return