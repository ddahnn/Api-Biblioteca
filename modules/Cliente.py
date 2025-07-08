from sqlalchemy import Column, String, Integer, Boolean, ForeignKey # type: ignore
from config.database import Base 

class Cliente(Base):
    __tablename__ = "cliente"

    matricula = Column(Integer,  index=True, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(11), nullable = False)