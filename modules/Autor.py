from sqlalchemy import Column, String, Integer # type: ignore
from config.database import Base 

class Autor(Base):
    __tablename__ = "autor"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    pais_origem = Column(String, nullable=False)
