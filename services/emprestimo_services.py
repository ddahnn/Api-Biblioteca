from sqlalchemy.orm import Session
from datetime import date, timedelta
from modules.Emprestimo import Emprestimo
from modules.Livro import Livro
from schemas.emprestimo_schema import EmprestimoCreate, EmprestimoDevolucao

def criar_emprestimo(db: Session, dados: EmprestimoCreate):
    emprestimos_ativos = db.query(Emprestimo).filter(
        Emprestimo.cliente_id == dados.cliente_id,
        Emprestimo.data_devolucao == None
    ).count()
    if emprestimos_ativos >= 3:
        raise Exception("Cliente já atingiu o limite de 3 livros emprestados.")
    livro = db.query(Livro).filter(Livro.isbn == dados.livro_id).first()
    if not livro or not livro.disponivel:
        raise Exception("Livro não disponível para empréstimo.")
    nova_data = date.today()
    devolucao_prevista = nova_data + timedelta(days=7)
    emprestimo = Emprestimo(
        cliente_id=dados.cliente_id,
        livro_id=dados.livro_id,
        data_retirada=nova_data,
        data_prevista_devolucao=devolucao_prevista
    )
    livro.disponivel = False
    db.add(emprestimo)
    db.commit()
    db.refresh(emprestimo)
    return emprestimo


def devolver_livro(db: Session, emprestimo_id: int, dados: EmprestimoDevolucao):
    emprestimo = db.query(Emprestimo).filter(Emprestimo.id == emprestimo_id).first()
    if not emprestimo:
        raise Exception("Empréstimo não encontrado.")
    if emprestimo.data_devolucao is not None:
        raise Exception("Esse livro já foi devolvido.")
    emprestimo.data_devolucao = dados.data_devolucao
    livro = db.query(Livro).filter(Livro.isbn == emprestimo.livro_id).first()
    if livro:
        livro.disponivel = True
    db.commit()
    db.refresh(emprestimo)
    atraso = 0
    if emprestimo.data_devolucao > emprestimo.data_prevista_devolucao:
        atraso = (emprestimo.data_devolucao - emprestimo.data_prevista_devolucao).days
    return {"mensagem": "Livro devolvido com sucesso", "dias_atraso": atraso}


def listar_emprestimos_por_cliente(db: Session, cliente_id: int):
    emprestimos = db.query(Emprestimo).filter(
        Emprestimo.cliente_id == cliente_id,
        Emprestimo.data_devolucao == None
    ).all()
    return emprestimos


def listar_todos_emprestimos_ativos(db: Session):
    return db.query(Emprestimo).filter(Emprestimo.data_devolucao == None).all()
