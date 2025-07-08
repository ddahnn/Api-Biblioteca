from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmprestimoBase(BaseModel):
    cliente_id: int
    livro_id: int

class EmprestimoCreate(EmprestimoBase):
  
    pass

class EmprestimoDevolucao(BaseModel):
    data_devolucao: date

class EmprestimoResponse(EmprestimoBase):
    id: int
    data_retirada: date
    data_prevista_devolucao: date
    data_devolucao: Optional[date] = None

    class Config:
        from_attributes = True
