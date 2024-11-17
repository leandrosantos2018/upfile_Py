from datetime import datetime

from pydantic import BaseModel

class Usuario(BaseModel):
    id:int
    username:str
    password:str


class UsuarioRequest(BaseModel):
    id: int
    usename: str


class TokenResponse(BaseModel):
    access_token: str



