from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str
    creator_id: int

class User (BaseModel):
    name: str
    email: str
    password: str

class ShowUser (BaseModel):
    name: str
    email: str
    blogs: List[Blog]

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None