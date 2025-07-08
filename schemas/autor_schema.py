from pydantic import BaseModel # type: ignore

class AutorBase(BaseModel):
    nome: str
    pais_origem: str

class AutorCreate(AutorBase):
    pass

class AutorUpdate(AutorBase):
    pass

class AutorResponse(AutorBase):
    id: int
    class Config:
        from_attributes = True
