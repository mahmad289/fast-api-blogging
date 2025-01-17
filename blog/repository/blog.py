from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Response, status
from .. import models, schemas

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body= request.body, creator_id = request.creator_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_by_id(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
    return blog
    
def delete(id: int, db:Session):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return {"detail":f"Blog with id: {id} deleted"}

def update (id:int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} not found')
    blog.body= request.body
    blog.title= request.title
    db.commit()
    db.refresh(blog)
    return blog
