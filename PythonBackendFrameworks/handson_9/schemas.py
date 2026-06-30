from pydantic import BaseModel
from pydantic import EmailStr


class Register(BaseModel):
    email: EmailStr
    password: str


class Login(BaseModel):
    email: EmailStr
    password: str