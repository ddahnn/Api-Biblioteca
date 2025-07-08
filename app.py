from fastapi import FastAPI # type: ignore
from config.database import Base, engine
from routes import autor_routes, livro_routes, cliente_routes, emprestimo_routes


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Biblioteca",
    version="1.0.0",
    description="API para gerenciamento de biblioteca (autores, livros, clientes, empréstimos)."
)

app.include_router(cliente_routes.router)
app.include_router(autor_routes.router)
app.include_router(livro_routes.router)
app.include_router(emprestimo_routes.router)