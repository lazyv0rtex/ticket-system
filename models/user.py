from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    username: str
    password: str

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    username: str

class UserLogin(BaseModel):
    username_or_email: str
    password: str
