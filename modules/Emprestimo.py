from datetime import date
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Emprestimo(Base):
    __tablename__ = "emprestimo"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("cliente.matricula"))
    livro_id = Column(Integer, ForeignKey("livro.isbn"))
    data_retirada = Column(Date, default=date.today)
    data_prevista_devolucao = Column(Date)
    data_devolucao = Column(Date, nullable=True)


    livro = relationship("Livro")
    cliente = relationship("Cliente")
