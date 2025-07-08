from pydantic import BaseModel # type: ignore
from typing import Optional

class ClienteBase(BaseModel):
    nome: str
    telefone:str

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome:Optional[str] = None
    telefone:Optional[str] = None

class ClienteResponse(ClienteBase):
    matricula:int

    class Config:
        from_attributes = True