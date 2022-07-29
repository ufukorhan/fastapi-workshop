from pydantic import BaseModel
from datetime import datetime

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
