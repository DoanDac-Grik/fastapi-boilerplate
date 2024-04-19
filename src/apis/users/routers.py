from typing import Annotated
from fastapi import APIRouter, Depends, Query, Path
from sqlmodel import Session

from src.common.constants import DEFAULT_LIMIT_PAGE, DEFAULT_PAGE
from src.apis.users.models import BodyCreateDto, BodyUpdateDto
from src.common.response import PaginationResponseData, ResponseData
from src.configs.database import get_session
from src.apis.users.controllers import UserController

router = APIRouter(prefix='/users')


@router.post("")
def create(payload: BodyCreateDto, db: Session = Depends(get_session)):
    user = UserController.create(payload, db)
    return ResponseData(user)

@router.get("")
def list(
    limit: Annotated[int | None, Query(gt=0)] = DEFAULT_LIMIT_PAGE, 
    page: Annotated[int | None, Query(gte=0 )] = DEFAULT_PAGE, 
    db: Session = Depends(get_session),
):
    users, total_pages = UserController.list(limit, page, db)
    return PaginationResponseData(users, limit, page, total_pages)
    
@router.get("/{id}")
def get_by_id(
    id: Annotated[int, Path(title="User ID")],  
    db: Session = Depends(get_session),
):
    user = UserController.get_by_id(id, db)
    return ResponseData(user)

@router.patch("/{id}")
def update_by_id(
    id: Annotated[int, Path(title="User ID")],
    payload: BodyUpdateDto, 
    db: Session = Depends(get_session),
):
    updated_user = UserController.update_by_id(id, payload, db)
    return ResponseData(updated_user)

@router.delete("/{id}")
def delete_by_id(
    id: Annotated[int, Path(title="User ID")],  
    db: Session = Depends(get_session),
):
    UserController.delete_by_id(id, db)
    return ResponseData({"success": True})