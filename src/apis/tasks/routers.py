from typing import Annotated
from fastapi import APIRouter, Depends, Query, Path
from sqlmodel import Session

from src.common.constants import DEFAULT_LIMIT_PAGE, DEFAULT_PAGE
from src.apis.tasks.models import BodyCreateDto, BodyUpdateDto
from src.common.response import PaginationResponseData, ResponseData
from src.configs.database import get_session
from src.apis.tasks.controllers import TaskController

router = APIRouter(prefix='/tasks')


@router.post("")
def create(payload: BodyCreateDto, db: Session = Depends(get_session)):
    task = TaskController.create(payload, db)
    return ResponseData(task)

@router.get("")
def list(
    limit: Annotated[int | None, Query(gt=0)] = DEFAULT_LIMIT_PAGE, 
    page: Annotated[int | None, Query(gte=0 )] = DEFAULT_PAGE, 
    db: Session = Depends(get_session),
):
    tasks, total_pages = TaskController.list(limit, page, db)
    return PaginationResponseData(tasks, limit, page, total_pages)
    
@router.get("/{id}")
def get_by_id(
    id: Annotated[int, Path(title="Task ID")],  
    db: Session = Depends(get_session),
):
    task = TaskController.get_by_id(id, db)
    return ResponseData(task)

@router.patch("/{id}")
def update_by_id(
    id: Annotated[int, Path(title="Task ID")],
    payload: BodyUpdateDto, 
    db: Session = Depends(get_session),
):
    updated_task = TaskController.update_by_id(id, payload, db)
    return ResponseData(updated_task)

@router.delete("/{id}")
def delete_by_id(
    id: Annotated[int, Path(title="Task ID")],  
    db: Session = Depends(get_session),
):
    TaskController.delete_by_id(id, db)
    return ResponseData({"success": True})