import math
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from src.apis.users.models import BodyCreateDto, BodyUpdateDto, User
from src.configs.database import get_session

class UserController:
    def create(payload: BodyCreateDto, db: Session = Depends(get_session)):
        user_to_db = User.model_validate(payload)
        db.add(user_to_db)
        db.commit()
        db.refresh(user_to_db)
        return user_to_db
    
    def list(limit: int, page: int, db: Session = Depends(get_session)):
        users = db.exec(select(User).offset(page - 1).limit(limit)).all()

        total_users = len(db.exec(select(User)).all())
        total_pages = math.ceil(total_users/limit)
       
        return users, total_pages
    
    def get_by_id(id:int, db: Session = Depends(get_session)):
        user = db.get(User, id)
        
        if not user:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "User not found"
            )
        
        return user
    
    def update_by_id(id:int, payload: BodyUpdateDto, db: Session = Depends(get_session)):
        user_to_update = db.get(User, id)
        if not user_to_update:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "User not found"
            )

        task_data =  payload.model_dump(exclude_unset=True)
        for key, value in task_data.items():
            setattr(user_to_update, key, value)
        
        db.add(user_to_update)
        db.commit()
        db.refresh(user_to_update)

        return user_to_update

    def delete_by_id(id:int, db: Session = Depends(get_session)):
        user = db.get(User, id)
        
        if not user:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "User not found"
            )
        
        db.delete(user)
        db.commit()

        return