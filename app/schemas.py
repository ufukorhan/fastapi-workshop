from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel): # Request Model
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase): # Request Model
    pass

class Post(PostBase): # Response Model
    id: int
    created_at: datetime

    class Config: # Pydantic's orm_mode will tell the Pydantic model to read data even if it is not a dict, but an ORM model(or any other arbitary object with attirubutes)
        orm_mode = True

class UserCreate(BaseModel): # Request Model
    email: EmailStr
    password: str

class UserOut(BaseModel): # Response Model
    id: int
    email: EmailStr
    created_at: datetime


    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None