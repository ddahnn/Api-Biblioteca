# 📚 API Biblioteca – FastAPI + PostgreSQL

Este projeto é uma API RESTful desenvolvida com **FastAPI** e **PostgreSQL**, com o objetivo de simular o sistema de controle de uma biblioteca.

---

## 🧩 Funcionalidades

- ✅ CRUD de Autores
- ✅ CRUD de Livros
- ✅ CRUD de Clientes
- ✅ Empréstimo de livros:
  - Um cliente pode emprestar até **3 livros ao mesmo tempo**
  - Apenas livros disponíveis podem ser emprestados
  - Ao devolver, o sistema registra a **data de devolução** e verifica se houve **atraso**
- ✅ Listagem de livros emprestados por cliente
- ✅ Listagem de todos os empréstimos ativos
- ✅ Testes no Insomnia e automatizados com pytest

---

## 🚀 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
- pytest

---

## ⚙️ Como executar o projeto

### Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL rodando com:
  - porta: **1234**
  - usuário: **postgres**
  - senha: **1234**
  - banco: **biblioteca**

### 1. Clone o repositório

```bash
git clone https://github.com/ddahnn/trabalho-api-biblioteca.git
cd trabalho-api-biblioteca

2. Crie e ative o ambiente virtual

python -m venv .venv
.venv\Scripts\activate  # (Windows)

3. Instale as dependências

pip install -r requirements.txt

4. Execute a API

uvicorn app:app --reload

Depois, acesse: http://localhost:8000/docs
✅ Testes
Testes manuais com Insomnia/Postman

    Os endpoints foram testados manualmente via Insomnia.

Testes automatizados com pytest

pytest tests/

👨‍💻 Autor

    Daniel (Dahn)

---
