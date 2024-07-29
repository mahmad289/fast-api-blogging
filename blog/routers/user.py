from typing import List
from .. import schemas, models, database, hashing
from fastapi import APIRouter, Depends, HTTPException, Response, status
from ..repository import user

from sqlalchemy.orm import Session

router = APIRouter (
    prefix="/user",
    tags=["User"]
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session= Depends(database.get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code=200,response_model=schemas.ShowUser)
def get_user(id:int, db: Session= Depends(database.get_db)):
    return user.get_by_id(id, db)
