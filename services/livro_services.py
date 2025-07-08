from sqlalchemy.orm import Session # type: ignore
from modules.Livro import Livro
from schemas.livro_schema import LivroCreate, LivroUpdate

def criar_Livro(db:Session, livro:LivroCreate):
    novo_livro = Livro(**livro.dict())
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro

def listar_Livro(db:Session):
    return db.query(Livro).all()

def buscar_Livro(db:Session, isbn:int):
    return db.query(Livro).filter(Livro.isbn == isbn).first()

def atualizar_Livro(db: Session, isbn: int, dados: LivroUpdate):
    livro = db.query(Livro).filter(Livro.isbn == isbn).first()
    if not livro:
        return None
    dados_dict = dados.dict(exclude_unset=True) 
    for campo, valor in dados_dict.items():
        setattr(livro, campo, valor)
    db.commit()
    db.refresh(livro)
    return livro

def deletar_livro(db:Session, isbn:int):
    livro = db.query(Livro).filter(Livro.isbn == isbn).first()
    if livro:
        db.delete(livro)
        db.commit()
    return livro