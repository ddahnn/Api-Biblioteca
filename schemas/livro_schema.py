from pydantic import BaseModel # type: ignore
from typing import Optional

class LivroBase(BaseModel):
    titulo: str
    ano_publicacao: int
    editora: str
    disponivel: Optional[bool] = True
    autor_id: int

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    ano_publicacao: Optional[int] = None
    editora: Optional[str] = None
    disponivel: Optional[bool] = None
    autor_id: Optional[int] = None

class LivroResponse(LivroBase):
    isbn: int

    class Config:
        from_attributes = True
