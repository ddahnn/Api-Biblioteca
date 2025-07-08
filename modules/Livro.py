from sqlalchemy import Column, String, Integer, Boolean, ForeignKey # type: ignore
from config.database import Base 

class Livro(Base):
    __tablename__ = 'livro'

    isbn = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    editora = Column(String(20), nullable =False)
    disponivel = Column(Boolean, default=True)

    autor_id = Column(Integer, ForeignKey('autor.id'), nullable=False)