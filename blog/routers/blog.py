from typing import List
from .. import schemas, models, database
from ..repository import blog
from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session

router = APIRouter (
    prefix="/blog",
    tags=["Blog"]
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session= Depends(database.get_db)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy (id: int, db: Session= Depends(database.get_db)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session= Depends(database.get_db)):
    return blog.update(id, request, db)

@router.get('/',response_model=List[schemas.ShowBlog], tags=["Blog"])
def all(db: Session= Depends(database.get_db)):
    return blog.get_all(db)

@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog, tags=["Blog"])
def show(id:int ,response:Response, db: Session= Depends(database.get_db)):
    return blog.get_by_id(id, db)