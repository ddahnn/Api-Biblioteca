from fastapi.testclient import TestClient
from datetime import date
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from app import app



client = TestClient(app)

def test_criar_emprestimo_sucesso():
    # Criar cliente
    client.post("/cliente/criar", json={
        "matricula": 999,
        "nome": "Cliente Teste",
        "telefone": "51999999999"
    })

    # Criar autor e livro
    autor = client.post("/autores/criar/", json={
        "nome": "Autor do Livro Emprestado",
        "pais_origem": "Brasil"
    }).json()

    livro = client.post("/livros/criar/", json={
        "titulo": "Livro Emprestável",
        "ano_publicacao": 2022,
        "editora": "Editora Legal",
        "autor_id": autor["id"]
    }).json()

    # Criar empréstimo
    resposta = client.post("/emprestimos/retirar", json={
        "cliente_id": 999,
        "livro_id": livro["isbn"]
    })

    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["cliente_id"] == 999
    assert dados["livro_id"] == livro["isbn"]


def test_devolver_livro():
    # Busca empréstimos ativos
    ativos = client.get("/emprestimos/ativos").json()
    if not ativos:
        return  # Nenhum empréstimo pra devolver

    emprestimo_id = ativos[0]["id"]

    resposta = client.put(f"/emprestimos/devolver/{emprestimo_id}", json={
        "data_devolucao": str(date.today())
    })

    assert resposta.status_code == 200
    assert "mensagem" in resposta.json()
