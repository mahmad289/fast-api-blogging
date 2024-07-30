from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models, hashing
from .database import engine, SessionLocal, get_db
from .routers import blog, user, authentication

from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
    
