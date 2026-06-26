from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):
    name:str
    code:str
    credits:int

class CourseUpdate(BaseModel):
    name:Optional[str]=None
    code:Optional[str]=None
    credits:Optional[int]=None

class CourseResponse(BaseModel):
    id:int
    name:str
    code:str
    credits:int

    class Config:
        from_attributes=True