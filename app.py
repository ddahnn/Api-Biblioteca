from fastapi import FastAPI # type: ignore
from config.database import Base, engine
from routes import autor_routes, livro_routes, cliente_routes, emprestimo_routes


from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from config.database import Base, engine
from routes import autor_routes, livro_routes, cliente_routes, emprestimo_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Biblioteca",
    version="1.0.0",
    description="API para gerenciamento de biblioteca (autores, livros, clientes, empréstimos)."
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(cliente_routes.router)
app.include_router(autor_routes.router)
app.include_router(livro_routes.router)
app.include_router(emprestimo_routes.router)
