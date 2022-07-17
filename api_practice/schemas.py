from pydantic import BaseModel
from typing import Optional


class HealthCheckStatus(BaseModel):
    is_server_running: bool


class UserSchema(BaseModel):
    user_name: str
    email_id: str
    password: str


class ShowUser(BaseModel):
    user_name: str
    email_id: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
